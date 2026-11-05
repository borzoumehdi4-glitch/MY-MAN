"""Offline tests for feed.py (no network, no third-party deps).

Usage: python3 test_feed.py
"""
import feed

# The layout that broke the first version: a feature card whose inner links
# ("Read this article") sit inside the card, so a naive `</a>` match truncates it.
HUGE_CARD = """
<a href="https://think.ing.com/articles/fx-daily-can-france-wake-up-ecb-doves/" class="card card-hor card-huge card-huge-imageright card-article  w-100">
    <div class="card-header ps-lg-5 bg-transparent border-0">
        <div class="entry-category-wrapper">
            <span class="entry-category">
                FX
            </span>
        </div>
        <div class="card-entry-date" data-date-raw="1793259600">
            Today, 07:40
        </div>
    </div>
    <div class="card-body py-0">
        <h3 class="card-title font-ing-display display-4">
            FX Daily: Can France wake up the ECB doves?
        </h3>
    </div>
    <div class="card-footer">
        <object><a href="https://think.ing.com/articles/fx-daily-can-france-wake-up-ecb-doves/" class="btn btn-dark btn-chevron d-inline">
            Read this <span class="text-lowercase">Article</span>
        </a></object>
    </div>
</a>
"""

SNAP_CARD = """
<a href="https://think.ing.com/snaps/ecb-keeps-rates-on-hold-as-christine-lagarde-announced-her-resignation/" class="card card-large card-article  mb-3 mb-lg-4">
    <div class="entry-category-wrapper">
        <span class="entry-category"> Rates </span>
        <span class="entry-category"> Eurozone </span>
    </div>
    <div class="card-entry-date" data-date-raw="1793174340">Yesterday</div>
    <p class="card-title font-ing-display fs-2 lh-sm mt-1">
        ECB keeps rates on hold as Lagarde announces resignation
    </p>
    <p class="card-text fs-large mb-0">
        Headline inflation is still little affected by higher energy prices
    </p>
</a>
"""

RSS = """<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0" xmlns:dc="http://purl.org/dc/elements/1.1/">
  <channel>
    <item>
      <title>Lagarde&rsquo;s comments point to a December ECB rate hike</title>
      <link>https://think.ing.com/articles/lagarde-comments-point-to-december-ecb-rate-hike/</link>
      <description>Upside risks to inflation complicate the ECB's job</description>
      <subject>Rates</subject>
      <date>2026-10-29T14:20:00+00:00</date>
    </item>
    <item>
      <title>RBA set to hike as inflation proves more stubborn</title>
      <link>https://think.ing.com/articles/rba-set-to-hike/</link>
      <description>Australia only</description>
      <date>2026-10-29T09:00:00+00:00</date>
    </item>
  </channel>
</rss>
"""



def test_parse_cards_handles_feature_card():
    items = feed.parse_cards(HUGE_CARD, "fx")
    assert len(items) == 1, items
    card = items[0]
    assert card["title"] == "FX Daily: Can France wake up the ECB doves?", card["title"]
    assert card["date"] == "2026-10-29", card["date"]
    assert card["sections"] == ["fx"]
    assert card["tags"] == ["FX"]
    assert card["kind"] == "article"
    assert card["teaser"] == ""  # feature cards carry no teaser on the listing page


def test_parse_cards_snap():
    card = feed.parse_cards(SNAP_CARD, "rates")[0]
    assert card["kind"] == "snap", card["kind"]
    assert card["date"] == "2026-10-28", card["date"]
    assert card["tags"] == ["Rates", "Eurozone"], card["tags"]
    assert card["title"] == "ECB keeps rates on hold as Lagarde announces resignation"
    assert card["teaser"] == "Headline inflation is still little affected by higher energy prices"


def test_parse_cards_ignores_non_card_links():
    markup = '<a href="https://think.ing.com/articles/x/" class="btn">Read</a>' + SNAP_CARD
    assert len(feed.parse_cards(markup, "rates")) == 1


def test_normalise():
    assert feed.normalise("https://think.ing.com/articles/a/") == "https://think.ing.com/articles/a/"
    assert feed.normalise("https://think.ing.com/articles/a") == "https://think.ing.com/articles/a/"
    assert feed.normalise("https://think.ing.com/articles/a?x=1#top") == "https://think.ing.com/articles/a/"


def test_merge_combines_sections_and_tags():
    merged = feed.merge(
        [
            {"url": "u/", "title": "t", "teaser": "", "tags": ["FX"], "sections": ["fx"], "date": "2026-10-28"},
            {"url": "u/", "title": "t", "teaser": "", "tags": ["Rates"], "sections": ["rates"], "date": "2026-10-29"},
        ]
    )
    assert len(merged) == 1
    assert merged[0]["sections"] == ["fx", "rates"], merged[0]["sections"]
    assert merged[0]["tags"] == ["FX", "Rates"], merged[0]["tags"]
    assert merged[0]["date"] == "2026-10-29"


def test_new_papers_skips_known_urls():
    state = {"papers": [{"url": "https://think.ing.com/articles/fx-daily-can-france-wake-up-ecb-doves"}]}
    original = feed.collect
    feed.collect = lambda macro=False: feed.merge(
        feed.parse_cards(HUGE_CARD, "fx") + feed.parse_cards(SNAP_CARD, "rates")
    )
    try:
        new = feed.new_papers(state=state)
    finally:
        feed.collect = original
    assert len(new) == 1, new
    assert new[0]["url"].endswith("christine-lagarde-announced-her-resignation/")


def test_parse_rss_filters_by_keyword():
    items = feed.parse_rss(RSS)
    assert len(items) == 1, items
    assert items[0]["sections"] == ["macro"]
    assert items[0]["date"] == "2026-10-29"
    assert "December ECB rate hike" in items[0]["title"]
    assert items[0]["url"] == (
        "https://think.ing.com/articles/lagarde-comments-point-to-december-ecb-rate-hike/"
    )


def test_article_text_strips_chrome():
    body = (
        "<p>Body <b>text</b>.</p>"
        "<p>More &amp; more detail follows here, enough of it that the "
        "navigation marker near the end of the page really is in the tail.</p>"
    )
    html = (
        '<html><head><style>.x{}</style></head><body><nav>NAVJUNK</nav>'
        '<div class="content_builder">' + body +
        "In this article<p>NAVJUNK</p></div>"
        "<footer>FOOTJUNK</footer></body></html>"
    )
    original = feed.fetch
    feed.fetch = lambda url: html
    try:
        text = feed.article_text("https://think.ing.com/articles/x/")
    finally:
        feed.fetch = original
    assert text.startswith("Body text. More & more detail"), text
    assert "JUNK" not in text, text


def test_parse_rss_falls_back_to_page_date():
    rss = RSS.replace("<date>2026-10-29T14:20:00+00:00</date>", "")
    original = feed.article_date
    feed.article_date = lambda url: "2026-10-29"
    try:
        items = feed.parse_rss(rss)
    finally:
        feed.article_date = original
    assert items and items[0]["date"] == "2026-10-29", items


def test_validate_catches_duplicate_papers():
    import store

    state = {
        "papers": [
            {"id": "a", "url": "https://think.ing.com/articles/x/"},
            {"id": "a", "url": "https://think.ing.com/articles/x"},
        ],
        "stories": [],
        "changelog": [],
    }
    problems = store.validate(state)
    assert any("duplicate paper id" in p for p in problems), problems
    assert any("duplicate paper url" in p for p in problems), problems


SEED_ITEMS = [
    {"url": "https://think.ing.com/articles/known/", "title": "Known", "date": "2026-11-04",
     "sections": ["fx"], "kind": "article", "teaser": "already stored"},
    {"url": "https://think.ing.com/articles/below-floor/", "title": "Too old", "date": "2026-10-20",
     "sections": ["fx"], "kind": "article", "teaser": "before the floor"},
    {"url": "https://think.ing.com/articles/new-one/", "title": "New one", "date": "2026-11-04",
     "sections": ["fx"], "kind": "article", "teaser": "fresh teaser"},
    {"url": "https://think.ing.com/articles/new-two/", "title": "New two", "date": "2026-11-05",
     "sections": ["rates"], "kind": "snap", "teaser": "another fresh teaser"},
]

INGEST_STATE = {
    "papers": [{"id": "known", "url": "https://think.ing.com/articles/known/", "date": "2026-11-04"}],
    "stories": [{"id": "s", "scenarios": [{"name": "a", "probability": 60, "history": []}]}],
    "changelog": [],
}


def _with_fake_feed(items, fn):
    original = feed.collect
    feed.collect = lambda macro=False: items
    try:
        return fn()
    finally:
        feed.collect = original


def test_ingest_applies_floor_and_skips_known_urls():
    import ingest

    found = _with_fake_feed(SEED_ITEMS, lambda: ingest.candidates(INGEST_STATE))
    urls = [c["url"] for c in found]
    assert urls == [
        "https://think.ing.com/articles/new-one/",
        "https://think.ing.com/articles/new-two/",
    ], urls


def test_ingest_labels_summary_and_never_touches_probabilities():
    import copy
    import ingest

    state = copy.deepcopy(INGEST_STATE)
    added = _with_fake_feed(SEED_ITEMS, lambda: ingest.ingest(state))
    assert added == ["new-one", "new-two"], added
    for paper in state["papers"][1:]:
        assert paper["summary"].startswith("[auto] Mechanical summary"), paper["summary"]
        assert paper["story_ids"] == [], "ingest must not decide story links"
    assert state["stories"][0]["scenarios"][0]["probability"] == 60
    assert state["stories"][0]["scenarios"][0]["history"] == []
    assert len(state["changelog"]) == 1 and "Auto-ingest" in state["changelog"][0]["text"]


def test_ingest_cap_takes_oldest_first_so_nothing_starves():
    import ingest

    items = [
        {"url": "https://think.ing.com/articles/d{}a/".format(d), "title": "t{}".format(d),
         "date": "2026-11-{:02d}".format(d), "sections": ["fx"], "kind": "article", "teaser": "x"}
        for d in (20, 11, 15, 12, 19)
    ]
    state = {"papers": [], "stories": [], "changelog": []}
    added = _with_fake_feed(items, lambda: ingest.ingest(state, limit=3))
    assert added == ["d11a", "d12a", "d15a"], added


def test_unique_id_avoids_collisions():
    import ingest

    assert ingest.unique_id("abc", set()) == "abc"
    assert ingest.unique_id("abc", {"abc"}) == "abc-2"
    assert ingest.unique_id("abc", {"abc", "abc-2"}) == "abc-3"


def test_ingest_is_idempotent():
    import copy
    import ingest

    state = copy.deepcopy(INGEST_STATE)
    first = _with_fake_feed(SEED_ITEMS, lambda: ingest.ingest(state))
    second = _with_fake_feed(SEED_ITEMS, lambda: ingest.ingest(state))
    assert first == ["new-one", "new-two"], first
    assert second == [], second  # the same feed content must add nothing the second time
    urls = [p["url"] for p in state["papers"]]
    assert len(urls) == len(set(urls)), urls


def main():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    for test in tests:
        test()
        print("ok  ", test.__name__)
    print("\n{} tests passed".format(len(tests)))


if __name__ == "__main__":
    main()

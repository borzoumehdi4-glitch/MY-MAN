"""Source data for the 2026 nail-trend report (30 trends, 11 sources).

Single source of truth: build_report.py turns this into the HTML, CSV and
Markdown versions so the three downloads never drift apart.
"""

REPORT_DATE = "28 October 2026"
REPORT_TITLE = "30 Nail Trends for 2026"
REPORT_SUBTITLE = (
    "The shapes, shades, finishes and nail-art looks the industry is actually "
    "booking in 2026 - sourced from Vogue, Allure, Harper's Bazaar, ELLE, "
    "Good Housekeeping, Marie Claire, Who What Wear and salon-shape data."
)

SOURCES = {
    "ALLURE": ("Allure - The Biggest Nail Trends of 2026 Upgrade the Classics "
               "(Loren Savini, 17 Dec 2025)",
               "https://www.allure.com/story/nail-trends-2026"),
    "VOGUE": ("Vogue - The 7 Biggest Nail Trends of 2026, According to Nail Pros "
              "(Audrey Noble, 30 Dec 2025)",
              "https://www.vogue.com/article/nail-trends-2026"),
    "GH": ("Good Housekeeping - The 19 Nail Trends You'll See Everywhere This Year "
           "(Celia Shatzman, 9 Feb 2026)",
           "https://www.goodhousekeeping.com/beauty/nails/a70244342/2026-nail-trends/"),
    "HB": ("Harper's Bazaar UK - The 10 biggest nail trends you're going to see in 2026",
           "https://www.harpersbazaar.com/uk/beauty/make-up-nails/g69835470/nail-trends-2026/"),
    "WWW": ("Who What Wear - 6 Biggest Nail-Art Trends of 2026 "
            "(Grace Lindsay, 18 Jan 2026)",
            "https://www.whowhatwear.com/beauty/nails/nail-art-trends-2026"),
    "ELLE": ("ELLE UK - 8 Of The Biggest Nail Trends To Try In 2026 "
             "(Urmi Pandit, 24 Dec 2025)",
             "https://www.elle.com/uk/beauty/nails/a69925591/nail-trends-2026/"),
    "ALLURE_FALL": ("Allure - The Nail Color Trends of Fall 2026 "
                    "(Eden Stuart, 25 Aug 2026)",
                    "https://www.allure.com/story/fall-nail-color-trends-2026"),
    "MC": ("Marie Claire - 2026 Nail Trends Lean Into a Quieter Kind of Luxury "
           "(Marisa Petrarca, 31 Dec 2025)",
           "https://www.marieclaire.com/beauty/nails/nail-trends-2026/"),
    "MC_SPRING": ("Marie Claire - The 9 Best Spring Nail Trends "
                  "(Catharine Malzahn, 19 Feb 2026)",
                  "https://www.marieclaire.com/beauty/nails/spring-2026-nail-trends/"),
    "HB_RUNWAY": ("Harper's Bazaar - The 25 Nail Moments You Can't Miss from Fashion "
                  "Week (spring 2026 runways, Sep 2025)",
                  "https://www.harpersbazaar.com/beauty/nails/g66123007/best-nail-trends-spring-2026/"),
    "PURE": ("Pure Nails - The most requested nail shapes in 2026",
             "https://purenails.co.uk/blogs/news/the-most-requested-nail-shapes-in-2026"),
}

CATEGORIES = ["Finish & texture", "Colour", "Nail art", "Shape"]

THEMES = [
    ("Elevated simplicity",
     "The year's organising idea. \"People want their nails to feel clean, "
     "luxurious, and thoughtfully designed without being overly decorated,\" "
     "celebrity artist Kim Truong tells Vogue. Fewer elements, better executed."),
    ("Restraint plus one high-impact detail",
     "Townhouse's Juanita Huber-Millet calls 2026 \"elegant restraint\"; "
     "Queenie Nguyen describes \"light-reflective minimalism paired with "
     "hyper-textural statement art\". Translation: a sheer neutral base and a "
     "single sculptural, jewelled or pierced accent."),
    ("Texture beats colour",
     "Tweed, velvet, ribbed glass, chrome and 3D gel replaced last year's flat "
     "creams. Chanel under Matthieu Blazy is the reference point - boucle, "
     "woven and lace effects translated onto the nail."),
    ("Nail health is the flex",
     "\"Healthy nails always start with the natural nail,\" says Navy "
     "Professional founder Rebecca Crawforth. Builder gel/BIAB overlays, "
     "cuticle serum and shorter lengths are what make the sheer, milky looks "
     "possible."),
    ("Pantone sets the palette",
     "Cloud Dancer, Pantone's 2026 Colour of the Year, is an airy translucent "
     "white that anchors the year: it is the base under glitzy French tips, "
     "lace art, halo nails and micro dots."),
    ("Maximalism in controlled doses",
     "Allure's \"mixed maximalist\", ELLE's \"glitchy glam\" and Who What Wear's "
     "\"bold and bedazzled\" are the counter-current - mismatched hands, "
     "asymmetry and charms, usually across two or three accent nails."),
]

SEASON_CALENDAR = [
    ("Spring 2026", ["Cloud Dancer milky whites", "Ultra-sheer washes",
                     "Soft, slim & milky French", "Micro polka dots",
                     "Stripes & athletic-sock tips", "Soft square",
                     "Squoval & short-and-sweet", "Aqua and electric blues"]),
    ("Summer 2026", ["Juicy glass / jelly glow", "Blown & ribbed glass",
                     "Celestial & halo nails", "Molten & mirror metallics",
                     "Sculptural 3D accents", "Sculpted almond & oval",
                     "Maximalist mix & glitchy glam"]),
    ("Autumn 2026", ["Comfort neutrals", "Cool-toned browns / espresso",
                     "Earthy greens", "Matured reds", "Not-quite-black",
                     "Preppy plaid & argyle", "Textile textures",
                     "Animal print & bambicore"]),
    ("Winter 2026 / holiday", ["Glitzy French", "Nail piercing & hardware",
                               "Sapphire & electric blues", "Velvet chrome",
                               "Cat-eye magnetic 3D", "Molten metallics",
                               "Coffin & the cat-claw curve"]),
]

TRENDS = [
    {
        "n": 1, "cat": "Finish & texture",
        "name": "Cloud Dancer milky whites",
        "tagline": "Pantone's 2026 Colour of the Year, on your nails",
        "what": "Pantone named Cloud Dancer its 2026 Colour of the Year and the "
                "nail world translated it into a translucent, creamy white that "
                "reads as a milkshake glow rather than flat white-out. Artists "
                "keep it airy - two sheer coats over the natural nail, free edge "
                "still visible - and let gloss do the luxury part.",
        "palette": "Sheer creamy off-white (#F4F1EC to #E8E2D9), satin to high gloss",
        "shape": "Short almond, squoval or short round",
        "season": "All year; peaks spring/summer 2026",
        "wear": "Everyday / office-safe",
        "diff": 1,
        "ask": "Sheer milky white, two thin coats, no visible brushstrokes, high-gloss top coat.",
        "swatch": ["#F4F1EC", "#E8E2D9", "#D9CFC2"],
        "sources": ["GH", "ELLE", "HB", "MC"],
    },
    {
        "n": 2, "cat": "Finish & texture",
        "name": "Ultra-sheer washes",
        "tagline": "\"Your nails but better\" - the polished bare nail",
        "what": "Vogue lists ultra-sheer washes among its seven biggest trends: a "
                "single veil of warm pink, peach or tea-rose tint that evens out "
                "the nail bed without hiding it. Sundays Studio describes the "
                "effect as \"sunshine on water\" - warm, natural and flattering "
                "across skin tones, which is why it books year-round.",
        "palette": "Tea rose, peach and warm pink veils (#F6E4DE to #E6C3B8), gloss",
        "shape": "Any; best on short squoval or round",
        "season": "Spring/summer 2026, then a year-round staple",
        "wear": "Everyday / minimal",
        "diff": 1,
        "ask": "One coat of sheer warm pink, cuticle-clean, glass top coat - nothing opaque.",
        "swatch": ["#F6E4DE", "#EFD3CB", "#E6C3B8"],
        "sources": ["VOGUE", "HB", "MC_SPRING"],
    },
    {
        "n": 3, "cat": "Finish & texture",
        "name": "Juicy glass / jelly glow",
        "tagline": "The Korean jelly nail becomes the default neutral",
        "what": "Syrup-gel colour with a wet, see-through depth that makes nails "
                "read as \"juicy\". Good Housekeeping's experts call it \"the best "
                "version of a naked nail, but smooth and ultra shiny\"; on deeper "
                "skin tones it behaves as a glossed tint rather than a colour. "
                "ELLE files the same finish under \"glassy glow\".",
        "palette": "Syrupy rose, peach, cherry-cola, clear overlay (#F5D9CF to #D8A899)",
        "shape": "Short oval, squoval, medium almond",
        "season": "Spring/summer; returns as syrup browns in autumn",
        "wear": "Everyday to evening",
        "diff": 2,
        "ask": "Jelly/syrup gel in a translucent rose, three thin coats, high-build gloss top.",
        "swatch": ["#F5D9CF", "#E9C3B4", "#D8A899"],
        "sources": ["GH", "ELLE", "MC"],
    },
    {
        "n": 4, "cat": "Finish & texture",
        "name": "Soft chrome & pearl glaze",
        "tagline": "Chrome loses the mirror, gains the glow",
        "what": "Harper's Bazaar's Juanita Huber-Millet describes 2026 chrome as "
                "\"whisper-thin metallic washes over nudes, or pearlescent sheens "
                "layered over warm browns... less mirror shine, more soft "
                "luminosity\". It is the glazed-doughnut finish matured into "
                "something quieter and more expensive-looking.",
        "palette": "Pearl, champagne and soft silver washes (#DCD9D2 to #EFE9DF)",
        "shape": "Almond, oval or squoval; short works too",
        "season": "All year; peaks in party season",
        "wear": "Everyday to occasion",
        "diff": 2,
        "ask": "Pearl chrome powder over a warm nude - keep it a soft sheen, not mirror.",
        "swatch": ["#DCD9D2", "#C9C6BF", "#EFE9DF"],
        "sources": ["HB", "ELLE", "ALLURE_FALL"],
    },
    {
        "n": 5, "cat": "Finish & texture",
        "name": "Velvet chrome",
        "tagline": "Cat-eye velvet with a chrome overlay",
        "what": "Two 2026 favourites collided. Vogue predicts velvet nails finished "
                "with a cat-eye magnetic pull and a chrome overlay, giving a soft "
                "brush-stroke shimmer that shifts as the hand moves - all the "
                "texture of glitter with none of the grit. ILNP's Ritual and "
                "Kiss's Fine n Cool press-ons are the high-street route in.",
        "palette": "Dusty mauve, gunmetal and soft navy (#6E6A78 to #B9B2C4)",
        "shape": "Medium almond or oval - velvet reads best on longer beds",
        "season": "Autumn/winter 2026",
        "wear": "Evening / statement",
        "diff": 3,
        "ask": "Velvet cat-eye gel with a chrome topper, magnetic pull front to back.",
        "swatch": ["#6E6A78", "#9A94A6", "#B9B2C4"],
        "sources": ["VOGUE", "GH", "ELLE"],
    },
]

SALON_SCRIPT = [
    ("Milky base", "Sheer milky white, two thin coats, no visible brushstrokes, gloss top."),
    ("Bare-but-better", "One coat of sheer warm pink over the natural nail - nothing opaque."),
    ("Soft French", "Diffused French, very slim tip, off-white on milky, no harsh line."),
    ("Glazed neutral", "Pearl chrome powder over a warm nude - a soft sheen, not mirror."),
    ("Cat-eye velvet", "Cat-eye gel over a dark base, magnetic halo pull, chrome topper."),
    ("Stripes", "Two thin horizontal stripes across the tip, crisp edges, gloss."),
    ("Micro dots", "1-2 mm dots, evenly spaced, on a sheer milky base."),
    ("Hardware", "One gold ring through the free edge plus a stud at the base."),
    ("Shape", "Medium almond with the apex at the stress point - tapered, not pointed."),
    ("Shape (short)", "Short squoval, corners rounded, sheer colour, glass top coat."),
]

TRENDS += [
    {
        "n": 6, "cat": "Finish & texture",
        "name": "Cat-eye magnetic 3D",
        "tagline": "Pigment pulled into halos, bands and domes",
        "what": "Magnetic pigment is pulled with a magnet into a band, a halo or a "
                "3D dome. Artist Emi Kudo layers Apres Astral Gels over a dark "
                "base (Midnight Shadow) for a shimmer that looks lit from inside; "
                "Good Housekeeping notes the effect is now routinely combined with "
                "charms or a chrome overlay.",
        "palette": "Ink, plum, bronze or emerald bases with magnetic shimmer",
        "shape": "Almond, coffin, oval",
        "season": "Autumn/winter 2026, holiday",
        "wear": "Evening / statement",
        "diff": 3,
        "ask": "Cat-eye gel over a dark base, magnetic halo effect, no craft glitter.",
        "swatch": ["#2E2A3A", "#5B4B6E", "#8E7BA3"],
        "sources": ["GH", "VOGUE", "ELLE"],
    },
    {
        "n": 7, "cat": "Finish & texture",
        "name": "Molten & mirror metallics",
        "tagline": "Liquid metal, worn as jewellery",
        "what": "Full-coverage liquid metal - silver, gold, bronze - was the "
                "loudest finish of the fall 2026 shows and feeds the celestial "
                "trend. Allure's fall colour report names molten silver the "
                "season's \"treat yourself\" shade: it reads as jewellery on short "
                "nails and as armour on long almond or coffin tips.",
        "palette": "Molten silver, antique gold, bronze (#C8C9CC, #D4B878, #A9744F)",
        "shape": "Short squoval, or long almond/coffin",
        "season": "Fall/winter 2026, holiday",
        "wear": "Occasion / party",
        "diff": 2,
        "ask": "Full-coverage chrome or metallic silver, no glitter particles, mirror top coat.",
        "swatch": ["#C8C9CC", "#E6E7EA", "#A9744F"],
        "sources": ["ALLURE_FALL", "GH", "ELLE"],
    },
    {
        "n": 8, "cat": "Finish & texture",
        "name": "Blown & ribbed glass",
        "tagline": "The glass nail, sculpted instead of just shiny",
        "what": "Allure's \"blown glass\" and Good Housekeeping's \"ribbed glass\" "
                "push the glass nail into three dimensions: sculpted bubbles, fine "
                "ribs and holographic layers sealed under a clear dome. The spring "
                "2026 runways did the same thing at Head of State, where nails "
                "looked literally glass-blown.",
        "palette": "Clear, icy blue and pearl with holographic shifts",
        "shape": "Short-to-medium almond; sculpture needs length",
        "season": "Spring/summer 2026",
        "wear": "Statement / editorial",
        "diff": 5,
        "ask": "Clear builder gel sculpted into ribs or bubbles, holographic flake, high dome.",
        "swatch": ["#CDE7EA", "#E3F1F2", "#A8CFD5"],
        "sources": ["ALLURE", "GH", "HB_RUNWAY"],
    },
    {
        "n": 9, "cat": "Colour",
        "name": "Comfort neutrals",
        "tagline": "Caramel, chai and butter beige",
        "what": "Harper's Bazaar calls them \"comfort colours\": caramel, chai "
                "latte, buttery beige and warm mocha. Worn sheer-to-medium, these "
                "are what clients ask for when they want something cosier than a "
                "nude but safer than a colour - the palette equivalent of a "
                "cashmere throw.",
        "palette": "Caramel, chai, butter beige, mocha (#C8A279 to #E0C9AE)",
        "shape": "Any; almond and short squoval lead",
        "season": "Autumn/winter 2026",
        "wear": "Everyday / office",
        "diff": 1,
        "ask": "Warm caramel nude, sheer-to-medium coverage, gloss.",
        "swatch": ["#C8A279", "#B08968", "#E0C9AE"],
        "sources": ["HB", "MC"],
    },
    {
        "n": 10, "cat": "Colour",
        "name": "Cool-toned browns / espresso",
        "tagline": "Mocha cools down and goes deeper",
        "what": "The mocha of 2024-25 has cooled and deepened. Good Housekeeping "
                "flags cool-toned browns; Allure's fall 2026 report leads with "
                "\"cozy browns\" such as JinSoon Earth Clay (sent down Proenza "
                "Schouler) and Essie Never Skip a Beat, plus red-browns like Orly "
                "Canyon Clay. Marie Claire's autumn story is the same coffee "
                "mood.",
        "palette": "Cocoa, espresso, taupe-brown (#6B4B3A to #4A322A)",
        "shape": "Medium almond or square",
        "season": "Autumn/winter 2026",
        "wear": "Everyday to evening",
        "diff": 1,
        "ask": "Cool espresso brown, opaque, satin or gloss.",
        "swatch": ["#6B4B3A", "#8A6A57", "#4A322A"],
        "sources": ["GH", "ALLURE_FALL", "MC"],
    },
]

TRENDS += [
    {
        "n": 11, "cat": "Colour",
        "name": "Matured reds",
        "tagline": "Brick, bordeaux and cherry instead of bright tomato",
        "what": "Red, but grown up. Harper's Bazaar calls it \"matured reds\" - "
                "brick, wine and Bordeaux - while Allure's fall cherry is deeper "
                "still: Hermes Rouge H, Dazzle Dry Fast-Track Cherry and Nailboo's "
                "cola-toned Cola Kiss. Opaque, high-shine and unadorned; the "
                "colour is the whole design.",
        "palette": "Brick, bordeaux, merlot, cherry (#7E1F26 to #5C1218)",
        "shape": "Short almond or squoval; classic on oval",
        "season": "Autumn/winter 2026 (plus Valentine's)",
        "wear": "Everyday to evening",
        "diff": 1,
        "ask": "Deep bordeaux red, opaque, high-gloss - no shimmer.",
        "swatch": ["#7E1F26", "#A32638", "#5C1218"],
        "sources": ["HB", "ALLURE_FALL", "MC"],
    },
    {
        "n": 12, "cat": "Colour",
        "name": "Sapphire, electric & aqua blues",
        "tagline": "Jewel-box sapphire meets bright cobalt",
        "what": "Blue split into two moods: the sapphire of Allure's fall 2026 "
                "report (shades such as Sapphire Season and Playing With "
                "Sapphire) and the electric and aquamarine blues of spring. Good "
                "Housekeeping lists electric blue among the year's most-requested "
                "colours; ELLE's \"cool blue\" layers it under a silver chrome "
                "topper.",
        "palette": "Sapphire, electric cobalt, icy aquamarine (#1F3A6E, #2F6FB5, #7FC7D9)",
        "shape": "Short square or squoval for brights; almond for sapphire",
        "season": "Summer 2026 brights; winter 2026 sapphire",
        "wear": "Statement / holiday",
        "diff": 1,
        "ask": "Opaque sapphire (or electric cobalt), gloss; chrome topper optional.",
        "swatch": ["#1F3A6E", "#2F6FB5", "#7FC7D9"],
        "sources": ["GH", "ELLE", "ALLURE_FALL", "MC_SPRING"],
    },
    {
        "n": 13, "cat": "Colour",
        "name": "Earthy greens",
        "tagline": "Olive, moss and chartreuse",
        "what": "Olive, moss and chartreuse moved from the runway to the fingers. "
                "Allure's fall 2026 greens - Lights Lacquer Extra Dirty, Gel "
                "Jukebox Olive, The Stranger - are muddy and wearable; Marie "
                "Claire puts chartreuse at the loud end of the same family. Matte "
                "top coat makes them read modern rather than retro.",
        "palette": "Olive, moss, chartreuse (#6B6B3A, #4E5B31, #A8B36A)",
        "shape": "Short squoval; chartreuse on almond",
        "season": "Autumn 2026",
        "wear": "Everyday to statement",
        "diff": 1,
        "ask": "Muddy olive green, opaque, matte or satin top coat.",
        "swatch": ["#6B6B3A", "#4E5B31", "#A8B36A"],
        "sources": ["ALLURE_FALL", "MC"],
    },
    {
        "n": 14, "cat": "Colour",
        "name": "Not-quite-black",
        "tagline": "Black that reveals its colour in daylight",
        "what": "The compromise between black and colour: near-black plum, "
                "midnight navy and oxblood that read black indoors and show their "
                "hue in sunlight. Allure's fall list bundles Essie Wicked, OPI "
                "Lincoln Park After Dark and Manucurist Hollyhock; the winter "
                "pedicure story pushes the same idea into multichrome.",
        "palette": "Near-black plum, midnight navy, oxblood (#1A1418 to #2B1E26)",
        "shape": "Short oval, almond, square",
        "season": "Autumn/winter 2026",
        "wear": "Evening / everyday for the bold",
        "diff": 1,
        "ask": "Near-black plum, two coats, gloss - dark but not flat black.",
        "swatch": ["#1A1418", "#2B1E26", "#0E0B10"],
        "sources": ["ALLURE_FALL", "MC"],
    },
    {
        "n": 15, "cat": "Colour",
        "name": "Cloudy pastels",
        "tagline": "Lilac, butter yellow and peach blossom",
        "what": "The \"Goldilocks\" shades Allure describes as neither summery-"
                "bright nor wintry-dark. Lilac was fall 2026's surprise, butter "
                "yellow keeps rolling through 2026 and Marie Claire's spring list "
                "adds peach blossom and powder pink - all best in a cloudy, milky "
                "finish rather than a flat creme.",
        "palette": "Lilac, butter yellow, peach blossom, powder pink (#C9B8D8, #F3E3A8, #F6D3C4)",
        "shape": "Short almond or squoval",
        "season": "Spring 2026 into early autumn",
        "wear": "Everyday",
        "diff": 1,
        "ask": "Cloudy lilac (or butter yellow) - sheer and milky, never neon.",
        "swatch": ["#C9B8D8", "#F3E3A8", "#F6D3C4"],
        "sources": ["ALLURE_FALL", "MC_SPRING"],
    },
]

TRENDS += [
    {
        "n": 16, "cat": "Nail art",
        "name": "Stripes & athletic-sock tips",
        "tagline": "2026's successor to the polka dot",
        "what": "Allure's number-one art trend: pinstripes, barcode stripes, "
                "awning stripes and the \"athletic sock\" tip Miss Pop painted at "
                "Alice + Olivia spring/summer 2026 - two thin horizontal lines "
                "across a bare or white tip. Good Housekeeping's retro striped "
                "French stacks colour bands instead of one solid tip.",
        "palette": "Contrast pairs: red/white, black/cream, navy/pink",
        "shape": "Square or squoval - stripes need a straight tip",
        "season": "Spring/summer 2026; sports-luxe all year",
        "wear": "Statement / everyday",
        "diff": 3,
        "ask": "Two thin horizontal stripes across the tip, crisp edges, gloss.",
        "swatch": ["#E8E2D9", "#B3202A", "#2B2B2B"],
        "sources": ["ALLURE", "GH", "HB_RUNWAY"],
    },
    {
        "n": 17, "cat": "Nail art",
        "name": "Micro polka dots",
        "tagline": "The dot shrinks to 1-2 mm",
        "what": "After 2025's full-size dots, 2026 does them micro: one or two "
                "millimetre spots in a scattered or grid layout, or a single dot "
                "per nail. ELLE names micro polka dots among its eight biggest "
                "trends, and Good Housekeeping points out a toothpick is enough to "
                "DIY the whole set.",
        "palette": "Monochrome, tonal nudes, or one accent colour on Cloud Dancer white",
        "shape": "Short round or squoval",
        "season": "Spring/summer 2026",
        "wear": "Everyday",
        "diff": 2,
        "ask": "Micro dots, 1-2 mm, evenly spaced, on a sheer milky base.",
        "swatch": ["#F7F0E6", "#8E1F2B", "#2B2B2B"],
        "sources": ["GH", "ELLE", "MC_SPRING"],
    },
    {
        "n": 18, "cat": "Nail art",
        "name": "Glitzy French",
        "tagline": "The French tip, set with stones",
        "what": "The French tip got jewellery: crystal-studded tips, silver studs "
                "and rhinestone rows over a crisp neutral base. \"It's like "
                "jewelry for your nails,\" artist Sofi Mazur tells Allure; Valeriia "
                "Telemaniuk recommends a proper crystal adhesive rather than "
                "sticking gems onto wet gel, which \"will pop off in two days\".",
        "palette": "Nude base plus clear crystal, silver or multicolour rhinestones",
        "shape": "Almond or square; short French also works",
        "season": "Holiday 2026, weddings, party season",
        "wear": "Occasion",
        "diff": 4,
        "ask": "Slim French tip covered in small crystals, set with crystal adhesive, no bulky gel.",
        "swatch": ["#F1E7DC", "#D9C7B8", "#E6D3A3"],
        "sources": ["ALLURE", "HB"],
    },
    {
        "n": 19, "cat": "Nail art",
        "name": "Soft, slim & milky French",
        "tagline": "Diffused tips, tonal instead of white-on-pink",
        "what": "The French softened: ultra-slim tips, diffused edges and tonal "
                "pairs - milky base with an off-white tip, or chocolate over "
                "caramel. Who What Wear's \"cloudy French\" and Good Housekeeping's "
                "\"milky French\" describe the same airbrushed edge, and it is the "
                "most wearable nail-art trend of the year.",
        "palette": "Milky base + off-white tip; caramel + chocolate; sheer pink + white",
        "shape": "Short almond, oval or squoval",
        "season": "All year; peaks spring/summer",
        "wear": "Everyday / bridal / office",
        "diff": 2,
        "ask": "Soft diffused French, very thin tip, off-white on milky, no harsh line.",
        "swatch": ["#F3E4D8", "#8B5E3C", "#EFE9E1"],
        "sources": ["HB", "GH", "WWW", "ALLURE"],
    },
    {
        "n": 20, "cat": "Nail art",
        "name": "Preppy plaid & argyle",
        "tagline": "Ralph Lauren energy, painted on",
        "what": "Vogue's prep-school plaid and Good Housekeeping's argyle ride the "
                "argyle-knit revival: jelly plaid, diamonds with fine criss-cross "
                "lines, or dark-academia colourways built from a jewel base. Kylie "
                "Jenner's jelly plaid by Zola Ganzorigt is the reference image "
                "clients bring to the salon.",
        "palette": "Jewel tones, burgundy, forest, cream with fine white lines",
        "shape": "Square, squoval or short almond",
        "season": "Autumn/winter 2026, peak December",
        "wear": "Statement / seasonal",
        "diff": 4,
        "ask": "Plaid or argyle: jelly base, thin white criss-cross lines, one accent diamond.",
        "swatch": ["#2F4A3C", "#A32638", "#E0C9AE"],
        "sources": ["VOGUE", "GH"],
    },
]

TRENDS += [
    {
        "n": 21, "cat": "Nail art",
        "name": "Textile textures: tweed, lace & silk",
        "tagline": "Runway fabric becomes a nail technique",
        "what": "Chanel under Matthieu Blazy is the reference: tweed, woven "
                "texture, lace and silk translated onto the nail. Vogue lists both "
                "Chanel tweed and lace-and-silk among its seven trends; Who What "
                "Wear's lace art wears the same idea as an accent nail or under a "
                "French tip, with Cloud Dancer as the base.",
        "palette": "Boucle cream, tweed multi-tones, black lace over Cloud Dancer",
        "shape": "Short almond or oval - texture needs a small canvas",
        "season": "Autumn/winter 2026, couture mood",
        "wear": "Editorial / occasion",
        "diff": 5,
        "ask": "Hand-painted lace (or tweed) on one accent nail, matte top coat to fake fabric.",
        "swatch": ["#C7BFB2", "#8A7F6E", "#E4DACB"],
        "sources": ["VOGUE", "WWW"],
    },
    {
        "n": 22, "cat": "Nail art",
        "name": "Celestial & halo nails",
        "tagline": "Moon dust, crystals and a ring of colour",
        "what": "Two star-themed looks dominate. \"Extra celestial\" - silver "
                "metallic, crystals, 3D charms and hardware that reads outer space "
                "- was flagged by Pinterest for 2026; halo nails draw a ring of "
                "polish around the nail edge instead of a tip (Dua Lipa wore "
                "them). Both work as one accent nail or a full set.",
        "palette": "Moon-dust silver and pearl; halos in contrast brights",
        "shape": "Almond and oval for halo; any for celestial",
        "season": "Winter 2026 / party season",
        "wear": "Statement / evening",
        "diff": 3,
        "ask": "Silver chrome with a few crystals at the cuticle, or a 2 mm halo outline.",
        "swatch": ["#B9BCC4", "#E7E9EE", "#6C6F7A"],
        "sources": ["WWW", "ELLE", "MC"],
    },
    {
        "n": 23, "cat": "Nail art",
        "name": "Nail piercing & hardware",
        "tagline": "Rings, studs and bangles, worn on the nail",
        "what": "Actual jewellery: tiny rings, bars and studs pierced through the "
                "free edge or set into gel, plus Good Housekeeping's \"bangles "
                "nails\" - stacked gold, silver or rose-gold bands with gemstones. "
                "Allure pairs black polish with \"a piercing (or five)\". The look "
                "is punk rather than precious.",
        "palette": "Black, cherry or nude base plus gold/silver hardware",
        "shape": "Square or almond with enough free edge to pierce",
        "season": "Autumn/winter 2026",
        "wear": "Statement / editorial",
        "diff": 5,
        "ask": "One gold ring through the tip plus a stud at the base; drill and seal properly.",
        "swatch": ["#C9A24B", "#D8D9DC", "#2B2B2B"],
        "sources": ["ALLURE", "GH"],
    },
    {
        "n": 24, "cat": "Nail art",
        "name": "Sculptural 3D accents",
        "tagline": "3D, but quiet - pearls and soft gel swirls",
        "what": "Three dimensions, restrained: micro pearls, delicate studs, soft "
                "gel swirls and negative space instead of 2025's charm-heavy "
                "maximalism. Harper's Bazaar calls it \"sculpted minimalism\"; "
                "Good Housekeeping notes 3D gel swirls coated in chrome powder for "
                "a harder, more graphic finish.",
        "palette": "Tonal nudes with pearl, chrome or gold accents",
        "shape": "Short almond or squoval; keep sculpture to 1-2 nails",
        "season": "All year; wedding-heavy in summer",
        "wear": "Occasion / subtle statement",
        "diff": 4,
        "ask": "One sculpted pearl or chrome swirl per hand over a sheer nude, negative space.",
        "swatch": ["#F1EDE4", "#D8CEC0", "#A89E8E"],
        "sources": ["HB", "VOGUE", "GH", "WWW"],
    },
    {
        "n": 25, "cat": "Nail art",
        "name": "Animal print & bambicore",
        "tagline": "Leopard, deer print and horse motifs",
        "what": "Leopard, deer print and horse motifs - Good Housekeeping labels "
                "the trend \"bambicore\" - replace last year's tortoiseshell. "
                "Vogue's Chanel reference pushes a refined leopard in muted "
                "browns, and Marie Claire's October 2026 report confirms animal "
                "print as the season's art story. Keep it tonal so it reads "
                "expensive rather than fancy-dress.",
        "palette": "Camel, cocoa, cream and black spots",
        "shape": "Almond, oval or short square",
        "season": "Autumn/winter 2026",
        "wear": "Statement",
        "diff": 4,
        "ask": "Tonal leopard on two or three nails, brown on cream, tiny spots, matte top.",
        "swatch": ["#8A5A3B", "#C9A279", "#3E2B20"],
        "sources": ["GH", "VOGUE", "MC"],
    },
]

TRENDS += [
    {
        "n": 26, "cat": "Nail art",
        "name": "Maximalist mix & glitchy glam",
        "tagline": "Mismatched hands, on purpose",
        "what": "The counter-trend: mismatched hands, clashing colours, matte "
                "against shiny 3D, Y2K references. Allure's \"mixed maximalist\" "
                "and ELLE's \"glitchy glam\" describe the same instinct - "
                "deliberate asymmetry after years of clean-girl minimalism - and "
                "it is the easiest trend to DIY because there are no rules.",
        "palette": "Anything: one matte, one gloss and one metallic per set",
        "shape": "Mixed shapes across hands (short plus medium)",
        "season": "Summer 2026 festival season",
        "wear": "Statement",
        "diff": 4,
        "ask": "Mismatched set: one hand matte brights, one hand gloss nudes, same accent charm.",
        "swatch": ["#D64545", "#3F6E8C", "#E8C33A"],
        "sources": ["ALLURE", "ELLE", "WWW"],
    },
    {
        "n": 27, "cat": "Shape",
        "name": "Sculpted almond & elongated oval",
        "tagline": "Shape is the hero, colour is the support",
        "what": "The salon default for 2026. Harper's Bazaar's experts say shape "
                "is now \"the hero, with colour and art as supporting details\"; "
                "Vogue lists sculpted almond among its seven trends, and Pure "
                "Nails' 2026 shape report still puts almond as the single most-"
                "requested shape because it lengthens the hand without stiletto "
                "maintenance.",
        "palette": "Works with every finish; chrome and velvet look best",
        "shape": "Sculpted almond / elongated oval, medium length",
        "season": "All year",
        "wear": "Everyday to bridal",
        "diff": 2,
        "ask": "Medium almond, apex at the stress point, tapered but not pointed.",
        "swatch": ["#E4C7B4", "#C9A48C", "#A8826B"],
        "sources": ["HB", "VOGUE", "GH", "PURE"],
    },
    {
        "n": 28, "cat": "Shape",
        "name": "Soft square",
        "tagline": "The square comeback, with rounded corners",
        "what": "The surprise of the spring 2026 runways: square tips returned, "
                "but soft - gently rounded corners rather than the sharp 2000s "
                "block. Harper's Bazaar's runway report leads with square as "
                "spring's biggest shape story and notes extra-long coffin as its "
                "exaggerated cousin; Good Housekeeping lists square among the "
                "year's key shapes.",
        "palette": "Best with brights, stripes and French tips",
        "shape": "Soft square, short to medium",
        "season": "Spring/summer 2026, then all year",
        "wear": "Everyday",
        "diff": 2,
        "ask": "Soft square - straight sides, corners filed round, medium length.",
        "swatch": ["#D9CFC2", "#C4B6A6", "#EFE6DA"],
        "sources": ["HB_RUNWAY", "GH", "PURE"],
    },
    {
        "n": 29, "cat": "Shape",
        "name": "Squoval & short-and-sweet",
        "tagline": "The practical winner of 2026",
        "what": "Squoval is strong like a square, soft like an oval and the least "
                "likely to snag. ELLE calls it the \"Squoval Revival\"; Harper's "
                "Bazaar's \"short and sweet\" pairs it with sheer, milky colour; "
                "Pure Nails rates it the easiest shape to maintain and among the "
                "strongest - which is why it is the default for anyone with an "
                "active life.",
        "palette": "Sheers, milky whites, soft chromes",
        "shape": "Squoval / short oval",
        "season": "All year",
        "wear": "Everyday / office / active",
        "diff": 1,
        "ask": "Short squoval, rounded corners, sheer milky colour, glass top coat.",
        "swatch": ["#EFE4D8", "#E3D3C4", "#D3C0AE"],
        "sources": ["ELLE", "HB", "PURE", "GH"],
    },
    {
        "n": 30, "cat": "Shape",
        "name": "Coffin & the cat-claw curve",
        "tagline": "The statement shape at the far end",
        "what": "Extra-long coffin appeared at Knwls, and Naomi Yasuda built a "
                "curved, feline \"cat-claw\" shape for L'Enchanteur - a dramatic "
                "C-curve that follows the finger. Both are extension territory, "
                "and the shapes that carry chrome, molten metallics and 3D "
                "sculpture best.",
        "palette": "Chrome, molten metallic, 3D embellishment",
        "shape": "Coffin or cat-claw (curved)",
        "season": "Runway-led; holiday 2026",
        "wear": "Editorial / statement",
        "diff": 5,
        "ask": "Long coffin with a deep C-curve, or a cat-claw taper; expect extensions.",
        "swatch": ["#3A2E33", "#6B5A62", "#B9AEB4"],
        "sources": ["HB_RUNWAY", "PURE"],
    },
]

import pandas as pd
import streamlit as st

import store

st.set_page_config(page_title="ING Macro Scenarios", layout="wide")
state = store.load()

st.title("ING Macro Stories & Scenarios")

with st.sidebar:
    page = st.radio("View", ["Stories & scenarios", "Papers", "What changed", "Add paper"])
    st.caption(f"{len(state['papers'])} papers · {len(state['stories'])} stories")
    for p in store.validate(state):
        st.warning(p)

BADGE = {"base": "🟦 Base", "bull": "🟩 Upside", "bear": "🟥 Downside", "tail": "🟪 Tail"}

if page == "Stories & scenarios":
    if not state["stories"]:
        st.info("No stories yet. Paste ING articles in the chat and the analysis will appear here.")
    for s in state["stories"]:
        with st.container(border=True):
            st.subheader(s["name"])
            st.caption(f"Category: {s.get('category', '-')} · Updated {s.get('updated', '-')}")
            st.write(s["summary"])
            if s.get("pairs"):
                st.markdown("**Pairs affected:** " + ", ".join(s["pairs"]))
            cols = st.columns(max(len(s["scenarios"]), 1))
            for col, sc in zip(cols, s["scenarios"]):
                with col, st.container(border=True):
                    st.markdown(f"**{BADGE.get(sc.get('type'), '')} – {sc['name']}**")
                    st.metric("Probability", f"{sc['probability']}%",
                              delta=store.prob_shift(sc))
                    st.write(sc["description"])
                    if sc.get("triggers"):
                        st.markdown("*Watch:* " + "; ".join(sc["triggers"]))
                    if sc.get("fx_impact"):
                        st.markdown("*FX impact:* " + sc["fx_impact"])
            hist = [{"date": h["date"], sc["name"]: h["probability"]}
                    for sc in s["scenarios"] for h in sc.get("history", [])]
            if hist:
                df = pd.DataFrame(hist).groupby("date").first().sort_index().ffill()
                st.line_chart(df)

elif page == "Papers":
    for p in sorted(state["papers"], key=lambda p: p["date"], reverse=True):
        with st.expander(f"{p['date']} – {p['title']}"):
            if p.get("url"):
                st.markdown(f"[Source]({p['url']})")
            st.write(p["summary"])
            st.caption("Stories: " + ", ".join(p.get("story_ids", [])))

elif page == "What changed":
    for c in sorted(state["changelog"], key=lambda c: c["date"], reverse=True):
        st.markdown(f"**{c['date']}** – {c['text']}")

else:
    st.write("Save a paper into the inbox, then tell me in chat to process it.")
    title = st.text_input("Title")
    text = st.text_area("Paste article text or URL", height=300)
    if st.button("Save to inbox") and title and text:
        st.success(f"Saved to {store.save_inbox_text(title, text)}")

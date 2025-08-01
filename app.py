import streamlit as st
import json
from agents.problem_validator import run as validate
from agents.market_researcher import run as research
from agents.business_model_builder import run as build_model
from agents.risk_analyzer import run as analyze_risk

st.set_page_config(page_title="Startup Idea Evaluator", layout="wide")

st.title("🚀 Startup Idea Evaluator")
st.write("Enter your startup idea below and click **Evaluate** to get a comprehensive report.")

idea = st.text_area("Describe your startup idea", height=150)
if st.button("Evaluate"):
    if not idea.strip():
        st.warning("Please enter a startup idea to evaluate.")
    else:
        # Phase 1: Validation
        with st.spinner("Validating idea..."):
            validation = validate(idea)
        st.subheader("1) Validation")
        st.write(validation)

        # Phase 2: Market Research
        with st.spinner("Performing market research..."):
            market = research(validation)
        st.subheader("2) Market Research")

        # ——— Bordered flex container around the three metrics ———
        html = f"""
        <div style="
            border:1px solid black;
            padding:16px;
            border-radius:8px;
            display:flex;
            gap:16px;
            ">
        <div style="flex:1;">
            <h4 style="margin-bottom:8px;">Market Size</h4>
            <p style="margin-top:0;">{market.get('market_size', 'N/A')}</p>
        </div>
        <div style="flex:1;">
            <h4 style="margin-bottom:8px;">Growth Rate</h4>
            <p style="margin-top:0;">{market.get('growth_rate', 'N/A')}</p>
        </div>
        <div style="flex:1;">
            <h4 style="margin-bottom:8px;">Top Competitors</h4>
            <ul style="margin-top:0;">
            {"".join(f"<li>{c}</li>" for c in market.get('top_competitors', []))}
            </ul>
        </div>
        </div>
        """
        st.markdown(html, unsafe_allow_html=True)

        # with st.spinner("Performing market research..."):
        #     market = research(validation)
        # st.subheader("2) Market Research")
        # st.json(market)

        # Phase 3: Business Model
        with st.spinner("Building business model..."):
            business = build_model(market)
        st.subheader("3) Business Model")

        revenue = business.get("revenue_streams", [])
        costs   = business.get("cost_structure", [])
        segs    = business.get("customer_segments", [])

        # Wrap the whole block in a bordered container
        st.markdown("""
        <div style="
            border: 1px solid #ccc;
            padding: 16px;
            border-radius: 8px;
            margin-bottom: 24px;">
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### 💰 Revenue Streams")
            for r in revenue:
                if isinstance(r, dict):
                    st.write(f"**{r.get('name', '')}**: {r.get('description', '')}")
                else:
                    st.write(f"- {r}")

        with col2:
            st.markdown("### 🏗️ Cost Structure")
            for c in costs:
                if isinstance(c, dict):
                    st.write(f"**{c.get('name', '')}**: {c.get('description', '')}")
                else:
                    st.write(f"- {c}")

        with col3:
            st.markdown("### 👥 Customer Segments")
            for s in segs:
                if isinstance(s, dict):
                    st.write(f"**{s.get('name', '')}**: {s.get('description', '')}")
                else:
                    st.write(f"- {s}")

        # Close the bordered container
        st.markdown("</div>", unsafe_allow_html=True)




        # with st.spinner("Building business model..."):
        #     business = build_model(market)
        # st.subheader("3) Business Model")
        # revenue = business.get("revenue_streams", [])
        # costs   = business.get("cost_structure", [])
        # segs    = business.get("customer_segments", [])

        # col1, col2, col3 = st.columns(3)

        # with col1:
        #     st.markdown("### 💰 Revenue Streams")
        #     for r in revenue:
        #         if isinstance(r, dict):
        #             st.write(f"**{r.get('name', '')}**: {r.get('description', '')}")
        #         else:
        #             st.write(f"- {r}")

        # with col2:
        #     st.markdown("### 🏗️ Cost Structure")
        #     for c in costs:
        #         if isinstance(c, dict):
        #             st.write(f"**{c.get('name', '')}**: {c.get('description', '')}")
        #         else:
        #             st.write(f"- {c}")

        # with col3:
        #     st.markdown("### 👥 Customer Segments")
        #     for s in segs:
        #         if isinstance(s, dict):
        #             st.write(f"**{s.get('name', '')}**: {s.get('description', '')}")
        #         else:
        #             st.write(f"- {s}")


        # with st.spinner("Building business model..."):
        #     business = build_model(market)
        # st.subheader("3) Business Model")
        # st.json(business)

        # Phase 4: Risk Analysis
        with st.spinner("Analyzing risks..."):
            risks = analyze_risk(business)
        st.subheader("4) Risks & Mitigations")
        # display risks as table if list of dicts
        if isinstance(risks.get("risks"), list):
            st.table([{"Risk": r.get("risk"), "Mitigation": r.get("mitigation")} for r in risks["risks"]])
        else:
            st.json(risks)

        st.success("Evaluation complete!")

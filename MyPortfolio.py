import marimo as mo
import pandas as pd
import plotly.express as px

app = mo.App()

@app.cell
def imports():
    import marimo as mo
    import pandas as pd
    import plotly.express as px
    return mo, pd, px

@app.cell
def header(mo):
    return mo.md(
        """
        # Aryan Bahirwani
        ### BSc Accounting and Finance | Bayes Business School
        [LinkedIn](https://www.linkedin.com/in/aryan-bahirwani/) | [Email](mailto:aryan.bahirwani@bayes.city.ac.uk)
        """
    )

@app.cell
def navigation(mo, profile_tab, experience_tab, technical_tab):
    # This creates the tabbed layout like the example you sent
    return mo.ui.tabs({
        "👤 Profile": profile_tab,
        "💼 Experience": experience_tab,
        "💻 Technical Journey (Wk 4-9)": technical_tab
    })

@app.cell
def profile_section(mo):
    profile_tab = mo.vstack([
        mo.md("## Personal Statement"),
        mo.md(
            """
            I am a first-year Accounting and Finance student at City Saint George, University of London[cite: 1093, 1094]. 
            I am passionate about financial literacy and have a background in both corporate finance and non-profit leadership[cite: 1102, 1107].
            
            **Languages**: Hindi (Native), English (Fluent), Mandarin (Conversational)[cite: 1120].
            """
        )
    ])
    return profile_tab,

@app.cell
def experience_section(mo):
    experience_tab = mo.vstack([
        mo.md("## Professional Experience"),
        mo.md(
            """
            ### Finance Intern | Excel Asia AP Limited
            *March 2025 – May 2025*
            * Assisted in preparing annual company budgets and financial plans[cite: 1104].
            * Analysed monthly operational costs to improve spending efficiency[cite: 1105].
            
            ### Founder | Finance Future (Non-Profit)
            *Feb 2024 – Feb 2025*
            * Organized workshops on investment strategies and personal budgeting for 150 refugees[cite: 1110, 1111].
            
            ### Research & Awards
            * **Co-authored Research**: Studied human capital impact on GDP differences between Africa and Asia[cite: 1124].
            * **Wharton Investment Competition**: Achieved 18th place globally[cite: 1128].
            """
        )
    ])
    return experience_tab,

@app.cell
def technical_section(mo):
    # This section is CRITICAL for your grade (70+)
    technical_tab = mo.vstack([
        mo.md("## Technical Showcase (Weeks 4-9)"),
        mo.md(
            """
            ### Data Analysis & Reactivity (Week 4)
            Using Python and Pandas, I developed interactive dashboards to visualize S&P 500 data[cite: 9, 109]. 
            This demonstrates my ability to use **Vectorization** and **Reactive Data Filtering**[cite: 586, 588].
            
            ### Web Scraping (Week 7)
            I implemented automation pipelines using **Playwright** to crawl corporate websites and 
            extract data while bypassing bot detection[cite: 608, 620].
            
            ### AI & LLM APIs (Weeks 8 & 9)
            I utilized **Programmatic Prompting** via LLM APIs to conduct sentiment analysis on 
            annual reports[cite: 1043, 1059]. I employed **Few-shot examples** to ensure 
            consistent results[cite: 1070].
            """
        )
    ])
    return technical_tab,

if __name__ == "__main__":
    app.run()

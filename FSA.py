import streamlit as st
import pandas as pd
import random
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Financial Ratio Trainer",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .question-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 5px solid #1f77b4;
    }
    .feedback-correct {
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin: 1rem 0;
    }
    .feedback-incorrect {
        background-color: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #dc3545;
        margin: 1rem 0;
    }
    .ratio-explanation {
        background-color: #e7f3ff;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .new-problem-btn {
        background-color: #ff6b6b;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

class FinancialRatioTrainer:
    def __init__(self):
        self.company_names = [
            "Tech Innovations Inc.", "Global Manufacturing Corp.", "Retail Giant Co.",
            "Service Masters LLC", "Consumer Products Inc.", "Energy Solutions Ltd.",
            "Healthcare Systems Co.", "Logistics Express Inc.", "Finance Partners LLC",
            "Software Dynamics Corp."
        ]
        
    def generate_random_question(self, question_type):
        """Generate random financial data for different ratio types"""
        company = random.choice(self.company_names)
        
        if question_type == "current_ratio":
            current_assets = random.randint(200000, 1000000)
            # Ensure current ratio stays between 0.8 and 3.0 for realistic scenarios
            target_ratio = random.uniform(0.8, 3.0)
            current_liabilities = int(current_assets / target_ratio)
            
            return {
                "type": "current_ratio",
                "company": company,
                "scenario": f"You're analyzing the liquidity position of {company}. Calculate the Current Ratio to assess their short-term financial health.",
                "data": {
                    "Current Assets": current_assets,
                    "Current Liabilities": current_liabilities
                },
                "formula": "Current Ratio = Current Assets / Current Liabilities",
                "correct_answer": round(current_assets / current_liabilities, 2),
                "tolerance": 0.05,
                "interpretation": {
                    "good": "≥ 2.0 - Excellent liquidity position",
                    "average": "1.5 - 1.9 - Adequate liquidity",
                    "poor": "< 1.5 - Potential liquidity concerns"
                },
                "explanation": f"The current ratio measures a company's ability to pay short-term obligations. A ratio of {current_assets/current_liabilities:.2f} means the company has ${current_assets/current_liabilities:.2f} in current assets for every $1 of current liabilities."
            }
        
        elif question_type == "debt_to_equity":
            total_equity = random.randint(300000, 1500000)
            # Ensure debt-to-equity stays between 0.5 and 3.5 for realistic scenarios
            target_ratio = random.uniform(0.5, 3.5)
            total_liabilities = int(total_equity * target_ratio)
            
            return {
                "type": "debt_to_equity",
                "company": company,
                "scenario": f"As a credit analyst, you need to evaluate the capital structure risk of {company}. Calculate the Debt-to-Equity Ratio.",
                "data": {
                    "Total Liabilities": total_liabilities,
                    "Total Equity": total_equity
                },
                "formula": "Debt-to-Equity Ratio = Total Liabilities / Total Equity",
                "correct_answer": round(total_liabilities / total_equity, 2),
                "tolerance": 0.05,
                "interpretation": {
                    "good": "≤ 1.0 - Conservative financing",
                    "average": "1.1 - 2.0 - Moderate leverage",
                    "poor": "> 2.0 - High financial risk"
                },
                "explanation": f"This ratio shows the proportion of debt financing relative to equity. A ratio of {total_liabilities/total_equity:.2f} indicates the company uses {total_liabilities/total_equity:.2f} times as much debt as equity."
            }
        
        elif question_type == "gross_profit_margin":
            revenue = random.randint(800000, 2000000)
            # Ensure gross margin stays between 15% and 60% for realistic scenarios
            target_margin = random.uniform(0.15, 0.60)
            cogs = int(revenue * (1 - target_margin))
            
            return {
                "type": "gross_profit_margin",
                "company": company,
                "scenario": f"Evaluate {company}'s production efficiency and pricing strategy by calculating the Gross Profit Margin.",
                "data": {
                    "Revenue": revenue,
                    "Cost of Goods Sold": cogs
                },
                "formula": "Gross Profit Margin = (Revenue - COGS) / Revenue",
                "correct_answer": round(target_margin, 2),
                "tolerance": 0.01,
                "interpretation": {
                    "good": "≥ 40% - Strong pricing power/cost control",
                    "average": "20% - 39% - Moderate efficiency",
                    "poor": "< 20% - Weak margins, competitive pressures"
                },
                "explanation": f"Gross profit margin shows the percentage of revenue remaining after accounting for direct production costs. A {target_margin:.1%} margin means for every $1 of sales, the company keeps ${target_margin:.2f} as gross profit."
            }
        
        elif question_type == "return_on_equity":
            equity = random.randint(500000, 2000000)
            # Ensure ROE stays between 5% and 35% for realistic scenarios
            target_roe = random.uniform(0.05, 0.35)
            net_income = int(equity * target_roe)
            
            return {
                "type": "return_on_equity",
                "company": company,
                "scenario": f"As an investor, assess how efficiently {company} generates profits from shareholders' investments. Calculate Return on Equity (ROE).",
                "data": {
                    "Net Income": net_income,
                    "Average Shareholders' Equity": equity
                },
                "formula": "Return on Equity = Net Income / Average Shareholders' Equity",
                "correct_answer": round(target_roe, 2),
                "tolerance": 0.01,
                "interpretation": {
                    "good": "≥ 15% - Excellent profitability",
                    "average": "8% - 14% - Reasonable returns",
                    "poor": "< 8% - Poor use of equity"
                },
                "explanation": f"ROE measures how effectively management uses shareholders' money to generate profits. A {target_roe:.1%} ROE means the company generates ${target_roe:.2f} profit for every $1 of equity."
            }
        
        elif question_type == "inventory_turnover":
            cogs = random.randint(600000, 1800000)
            # Ensure inventory turnover stays between 3 and 12 for realistic scenarios
            target_turnover = random.uniform(3, 12)
            avg_inventory = int(cogs / target_turnover)
            
            return {
                "type": "inventory_turnover",
                "company": company,
                "scenario": f"Analyze the inventory management efficiency of {company} by calculating the Inventory Turnover Ratio.",
                "data": {
                    "Cost of Goods Sold": cogs,
                    "Average Inventory": avg_inventory
                },
                "formula": "Inventory Turnover = Cost of Goods Sold / Average Inventory",
                "correct_answer": round(target_turnover, 1),
                "tolerance": 0.1,
                "interpretation": {
                    "good": "≥ 8 - Excellent inventory management",
                    "average": "4 - 7 - Reasonable turnover",
                    "poor": "< 4 - Slow-moving inventory, potential obsolescence"
                },
                "explanation": f"This ratio shows how many times a company sells and replaces its inventory during a period. A ratio of {target_turnover:.1f} means the company turns over its inventory {target_turnover:.1f} times per year."
            }

    def generate_question_set(self, num_questions=5):
        """Generate a set of random questions"""
        ratio_types = [
            "current_ratio", "debt_to_equity", "gross_profit_margin", 
            "return_on_equity", "inventory_turnover"
        ]
        
        questions = []
        selected_types = random.sample(ratio_types, min(num_questions, len(ratio_types)))
        
        for i, ratio_type in enumerate(selected_types):
            question = self.generate_random_question(ratio_type)
            question["id"] = i + 1
            questions.append(question)
        
        return questions

    def display_question(self, question):
        st.markdown(f'<div class="question-box">', unsafe_allow_html=True)
        
        st.subheader(f"Question {question['id']}: {question['company']}")
        st.write(f"**Scenario:** {question['scenario']}")
        
        st.write("**Financial Data:**")
        data_df = pd.DataFrame(list(question['data'].items()), 
                             columns=['Item', 'Amount ($)'])
        # Format numbers with commas
        data_df['Amount ($)'] = data_df['Amount ($)'].apply(lambda x: f"{x:,}")
        st.dataframe(data_df, use_container_width=True)
        
        st.write(f"**Formula:** {question['formula']}")
        
        st.markdown('</div>', unsafe_allow_html=True)

    def check_answer(self, question, user_answer):
        correct_answer = question['correct_answer']
        tolerance = question['tolerance']
        
        if abs(user_answer - correct_answer) <= tolerance:
            st.markdown(f'<div class="feedback-correct">', unsafe_allow_html=True)
            st.success("✅ Correct! Well done!")
            st.markdown('</div>', unsafe_allow_html=True)
            return True
        else:
            st.markdown(f'<div class="feedback-incorrect">', unsafe_allow_html=True)
            st.error("❌ Incorrect. Let's review the solution.")
            st.markdown('</div>', unsafe_allow_html=True)
            return False

    def show_solution(self, question, user_answer):
        st.markdown(f'<div class="ratio-explanation">', unsafe_allow_html=True)
        
        st.subheader("📖 Solution & Explanation")
        
        # Show calculation steps
        st.write("**Calculation Steps:**")
        
        data = question['data']
        if question['type'] == 'current_ratio':
            current_assets = data['Current Assets']
            current_liabilities = data['Current Liabilities']
            st.write(f"Current Assets / Current Liabilities = ${current_assets:,} / ${current_liabilities:,}")
            st.write(f"= {current_assets / current_liabilities:.2f}")
            
        elif question['type'] == 'debt_to_equity':
            total_liabilities = data['Total Liabilities']
            total_equity = data['Total Equity']
            st.write(f"Total Liabilities / Total Equity = ${total_liabilities:,} / ${total_equity:,}")
            st.write(f"= {total_liabilities / total_equity:.2f}")
            
        elif question['type'] == 'gross_profit_margin':
            revenue = data['Revenue']
            cogs = data['Cost of Goods Sold']
            gross_profit = revenue - cogs
            st.write(f"Gross Profit = Revenue - COGS = ${revenue:,} - ${cogs:,} = ${gross_profit:,}")
            st.write(f"Gross Profit Margin = Gross Profit / Revenue = ${gross_profit:,} / ${revenue:,}")
            st.write(f"= {gross_profit / revenue:.2f} or {(gross_profit / revenue)*100:.1f}%")
            
        elif question['type'] == 'return_on_equity':
            net_income = data['Net Income']
            equity = data['Average Shareholders\' Equity']
            st.write(f"Net Income / Average Shareholders' Equity = ${net_income:,} / ${equity:,}")
            st.write(f"= {net_income / equity:.2f} or {(net_income / equity)*100:.1f}%")
            
        elif question['type'] == 'inventory_turnover':
            cogs = data['Cost of Goods Sold']
            inventory = data['Average Inventory']
            st.write(f"Cost of Goods Sold / Average Inventory = ${cogs:,} / ${inventory:,}")
            st.write(f"= {cogs / inventory:.1f} times")
        
        st.write("")
        st.write("**Interpretation Guidelines:**")
        for level, description in question['interpretation'].items():
            st.write(f"• **{level.title()}:** {description}")
        
        st.write("")
        st.write("**Business Insight:**")
        st.write(question['explanation'])
        
        st.markdown('</div>', unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="main-header">💰 Financial Ratio Analysis Trainer</h1>', unsafe_allow_html=True)
    st.write("### 🎯 Practice with unlimited randomly generated problems!")
    
    # Initialize session state
    if 'trainer' not in st.session_state:
        st.session_state.trainer = FinancialRatioTrainer()
    
    if 'questions' not in st.session_state:
        st.session_state.questions = st.session_state.trainer.generate_question_set()
    
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    
    if 'score' not in st.session_state:
        st.session_state.score = 0
    
    if 'answered' not in st.session_state:
        st.session_state.answered = False
    
    if 'total_attempted' not in st.session_state:
        st.session_state.total_attempted = 0
    
    if 'correct_answers' not in st.session_state:
        st.session_state.correct_answers = 0

    trainer = st.session_state.trainer
    questions = st.session_state.questions
    
    # Sidebar for navigation and progress
    with st.sidebar:
        st.header("📈 Progress Tracking")
        st.write(f"**Questions Completed:** {st.session_state.current_question}/{len(questions)}")
        st.write(f"**Session Score:** {st.session_state.score}")
        st.write(f"**Overall Accuracy:** {st.session_state.correct_answers}/{st.session_state.total_attempted} " + 
                f"({st.session_state.correct_answers/max(1, st.session_state.total_attempted)*100:.1f}%)")
        
        st.progress(st.session_state.current_question / len(questions))
        
        st.header("🔄 Problem Controls")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🔄 New Problem Set", use_container_width=True):
                st.session_state.questions = trainer.generate_question_set()
                st.session_state.current_question = 0
                st.session_state.score = 0
                st.session_state.answered = False
                st.rerun()
        
        with col2:
            if st.button("⏭️ Next Question", use_container_width=True) and st.session_state.current_question < len(questions) - 1:
                st.session_state.current_question += 1
                st.session_state.answered = False
                st.rerun()
        
        if st.session_state.current_question > 0:
            if st.button("⏮️ Previous Question", use_container_width=True):
                st.session_state.current_question -= 1
                st.session_state.answered = False
                st.rerun()
        
        if st.button("🔄 Reset Session", use_container_width=True):
            st.session_state.questions = trainer.generate_question_set()
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.session_state.total_attempted = 0
            st.session_state.correct_answers = 0
            st.rerun()
        
        st.header("💡 Tips")
        st.info("""
        - Round your answers to 2 decimal places
        - Read the scenario carefully
        - Check the formula before calculating
        - Practice regularly to improve!
        """)

    # Main content area
    current_q = st.session_state.current_question
    question = questions[current_q]
    
    trainer.display_question(question)
    
    # Answer input
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        user_answer = st.number_input(
            "Enter your answer:",
            min_value=0.0,
            max_value=1000.0,
            step=0.01,
            format="%.2f",
            key=f"answer_{current_q}"
        )
    
    with col2:
        if st.button("✅ Submit Answer", type="primary", use_container_width=True) and not st.session_state.answered:
            st.session_state.answered = True
            st.session_state.total_attempted += 1
            
            is_correct = trainer.check_answer(question, user_answer)
            if is_correct:
                st.session_state.score += 1
                st.session_state.correct_answers += 1
            
            trainer.show_solution(question, user_answer)
            st.rerun()
    
    # Show solution if already answered
    if st.session_state.answered:
        trainer.show_solution(question, user_answer)
    
    # Completion message
    if st.session_state.current_question == len(questions) - 1 and st.session_state.answered:
        st.balloons()
        accuracy = (st.session_state.correct_answers / st.session_state.total_attempted) * 100
        st.success(f"🎉 Congratulations! You've completed this problem set! Final Score: {st.session_state.score}/{len(questions)}")
        st.info(f"📊 Your overall accuracy: {accuracy:.1f}%")
        
        if accuracy >= 80:
            st.balloons()
            st.success("🏆 Excellent work! You've mastered financial ratios!")
        elif accuracy >= 60:
            st.success("👍 Good job! Keep practicing to improve!")
        else:
            st.warning("💪 Keep practicing! You'll get better with more practice.")

if __name__ == "__main__":
    main()

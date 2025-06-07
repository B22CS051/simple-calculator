import streamlit as st

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Simple Calculator",
        page_icon="🧮",
        layout="centered"
    )
    
    # App title and description
    st.title("🧮 Simple Calculator")
    st.markdown("---")
    st.write("Enter two numbers and select an operation to perform calculations.")
    
    # Create two columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        # Input for first number
        num1 = st.number_input(
            "Enter first number:",
            value=0.0,
            format="%.2f",
            key="num1"
        )
    
    with col2:
        # Input for second number
        num2 = st.number_input(
            "Enter second number:",
            value=0.0,
            format="%.2f",
            key="num2"
        )
    
    # Operation selection
    st.markdown("### Select Operation:")
    
    # Create columns for operation buttons
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("➕ Addition", use_container_width=True):
            st.session_state.operation = "+"
    
    with col2:
        if st.button("➖ Subtraction", use_container_width=True):
            st.session_state.operation = "-"
    
    with col3:
        if st.button("✖️ Multiplication", use_container_width=True):
            st.session_state.operation = "*"
    
    with col4:
        if st.button("➗ Division", use_container_width=True):
            st.session_state.operation = "/"
    
    # Alternative: Dropdown selection
    st.markdown("### Or use dropdown:")
    operation_dropdown = st.selectbox(
        "Choose operation:",
        ["Select an operation", "Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"],
        key="operation_dropdown"
    )
    
    # Map dropdown selection to operation symbol
    operation_map = {
        "Addition (+)": "+",
        "Subtraction (-)": "-",
        "Multiplication (*)": "*",
        "Division (/)": "/"
    }
    
    # Determine which operation to use
    if operation_dropdown != "Select an operation":
        operation = operation_map[operation_dropdown]
    elif 'operation' in st.session_state:
        operation = st.session_state.operation
    else:
        operation = None
    
    # Perform calculation and display result
    if operation:
        st.markdown("---")
        
        try:
            if operation == "+":
                result = num1 + num2
                operation_name = "Addition"
            elif operation == "-":
                result = num1 - num2
                operation_name = "Subtraction"
            elif operation == "*":
                result = num1 * num2
                operation_name = "Multiplication"
            elif operation == "/":
                if num2 == 0:
                    st.error("❌ Error: Division by zero is not allowed!")
                    return
                result = num1 / num2
                operation_name = "Division"
            
            # Display the calculation and result
            st.success(f"### 📊 Result:")
            st.markdown(f"**{operation_name}:** `{num1} {operation} {num2} = {result}`")
            
            # Show result in a nice metric format
            st.metric(
                label="Final Answer",
                value=f"{result:.4f}",
                delta=None
            )
            
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
    
    # Add some styling and information
    st.markdown("---")
    st.markdown("### 📝 Instructions:")
    st.markdown("""
    1. Enter your first number in the left input box
    2. Enter your second number in the right input box
    3. Click on an operation button OR select from the dropdown
    4. The result will appear automatically below
    """)
    
    # Add calculator history (optional feature)
    if st.checkbox("Show Calculation History"):
        if 'history' not in st.session_state:
            st.session_state.history = []
        
        if operation and 'result' in locals():
            # Add to history if not already there
            calculation = f"{num1} {operation} {num2} = {result}"
            if calculation not in st.session_state.history:
                st.session_state.history.append(calculation)
        
        if st.session_state.history:
            st.markdown("### 📋 History:")
            for i, calc in enumerate(reversed(st.session_state.history[-10:]), 1):
                st.text(f"{i}. {calc}")
            
            if st.button("Clear History"):
                st.session_state.history = []
                st.rerun()

if __name__ == "__main__":
    main()

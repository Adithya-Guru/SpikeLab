import streamlit as st
st.title("Classes and Modules")
with st.expander("Basic Setup", icon=":material/info:"):
    st.write("Welcome to Section 1: Setup! Before we can build complex robots that navigate mazes or solve timed missions on the mat, we must understand the basics of how Lego Spike Prime works. In this module, you will cover:")
    tab1, tab2, tab3, tab4 = st.tabs(["The Digital Workspace", "Parts of the Spike Kit", "The Electronics Inventory", "Check-In"])
    with tab1:
        st.write("Text")
    with tab2:
        st.write("Text")
    with tab3:
        st.write("Text")
    with tab4:
        st.write("Text")
with st.expander("Navigation", icon=":material/info:"):
    st.write("Text")
    tab1, tab2, tab3, tab4 = st.tabs(["Straight Movement", "The Art of Turning", "Driving Patterns", "Check-In"])
    with tab1:
        st.write("Text")
    with tab2:
        st.write("Text")
    with tab3:
        st.write("Text")
    with tab4:
        st.write("Content and .")
with st.expander("Sensors", icon=":material/info:"):
    st.write("Text")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["The Force Sensor", "The Distance Sensor", "The Color Sensor", "The Gyro Sensor", "Check-In"])
    with tab1:
        st.write("Text")
    with tab2:
        st.write("Text")
    with tab3:
        st.write("Text")
    with tab4:
        st.write("Text")
    with tab5:
        st.write("Text")
with st.expander("Attachments", icon=":material/info:"):
    st.write("Inside the expander.")
    tab1, tab2, tab3, tab4 = st.tabs(["The Motorized Arm", "Claws and Grippers", "Passive Attachments", "Check-In"])
    with tab1:
        st.write("Text")
    with tab2:
        st.write("Text")
    with tab3:
        st.write("Text")
    with tab4:
        st.write("Text")
with st.expander("Final Challenge", icon=":material/info:"):
    st.write("Text")
    tab1, tab2, tab3, tab4 = st.tabs(["Straight Movement", "The Art of Turning", "Driving Patterns", "Check-In"])
    with tab1:
        st.write("Text")
    with tab2:
        st.write("Text")
    with tab3:
        st.write("Text")
    with tab4:
        st.write("Text")
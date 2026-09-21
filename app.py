import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Configuration Rollback Recommendation System",
    page_icon="🔄",
    layout="wide"
)

if "apache" not in st.session_state:
    st.session_state.apache = True
    st.session_state.port = 80
    st.session_state.firewall = True
    st.session_state.status = "COMPLIANT"
    st.session_state.history = [
        {
            "time": datetime.now().strftime("%H:%M:%S"),
            "state": "Known-Good Configuration",
            "status": "COMPLIANT"
        }
    ]

st.title("🔄 Configuration Rollback Recommendation System")
st.caption("Rudder-Based Configuration Management & Rollback Prototype")

st.info(
    "This prototype demonstrates the Rudder workflow: "
    "Desired Configuration → Compliance Monitoring → Drift Detection → "
    "Rollback Recommendation → Restoration."
)

with st.sidebar:
    st.header("⚙️ System Information")
    st.write("**Configuration Tool:** Rudder")
    st.write("**Managed Service:** Apache")
    st.write("**Operating System:** Linux / Ubuntu")
    st.write("**Monitoring:** Configuration Compliance")
    st.write("**Purpose:** Configuration Rollback")

    st.divider()

    st.subheader("🎯 Desired Configuration")
    st.write("Apache: Running")
    st.write("Port: 80")
    st.write("Firewall: Enabled")

st.subheader("🖥️ Current Configuration")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Apache Service",
        "Running" if st.session_state.apache else "Stopped"
    )

with col2:
    st.metric(
        "Port",
        str(st.session_state.port)
    )

with col3:
    st.metric(
        "Firewall",
        "Enabled" if st.session_state.firewall else "Disabled"
    )

with col4:
    st.metric(
        "Compliance",
        st.session_state.status
    )

st.divider()

if st.session_state.status == "COMPLIANT":
    st.success(
        "✅ SYSTEM COMPLIANT — Current configuration matches the desired state."
    )

elif st.session_state.status == "NON-COMPLIANT":
    st.error(
        "❌ CONFIGURATION DRIFT DETECTED — Current configuration differs from the desired state."
    )

elif st.session_state.status == "RESTORED":
    st.success(
        "🔄 ROLLBACK SUCCESSFUL — Previous known-good configuration restored."
    )

if st.session_state.status == "NON-COMPLIANT":

    st.subheader("🚨 Detected Configuration Drift")

    drift_col1, drift_col2 = st.columns(2)

    with drift_col1:
        st.write("### Desired State")
        st.write("✔ Apache: Running")
        st.write("✔ Port: 80")
        st.write("✔ Firewall: Enabled")

    with drift_col2:
        st.write("### Current State")
        st.write(
            "✔ Apache: Running"
            if st.session_state.apache
            else "❌ Apache: Stopped"
        )
        st.write(f"❌ Port: {st.session_state.port}")
        st.write(
            "✔ Firewall: Enabled"
            if st.session_state.firewall
            else "❌ Firewall: Disabled"
        )

    st.warning(
        "Rudder would identify this node as NON-COMPLIANT "
        "and the previous known-good configuration can be recommended for restoration."
    )

    st.subheader("💡 Rollback Recommendation")

    st.info(
        "Recommended rollback configuration:\n\n"
        "• Apache → Running\n"
        "• Port → 80\n"
        "• Firewall → Enabled\n\n"
        "Reason: This represents the previous known-good configuration."
    )

st.subheader("🛠️ Configuration Actions")

button1, button2, button3 = st.columns(3)

with button1:
    if st.button("🚨 Simulate Configuration Drift", use_container_width=True):
        st.session_state.apache = False
        st.session_state.port = 9090
        st.session_state.firewall = True
        st.session_state.status = "NON-COMPLIANT"

        st.session_state.history.append(
            {
                "time": datetime.now().strftime("%H:%M:%S"),
                "state": "Configuration Drift Detected",
                "status": "NON-COMPLIANT"
            }
        )

        st.rerun()

with button2:
    if st.button("🔄 Apply Rollback", use_container_width=True):
        st.session_state.apache = True
        st.session_state.port = 80
        st.session_state.firewall = True
        st.session_state.status = "RESTORED"

        st.session_state.history.append(
            {
                "time": datetime.now().strftime("%H:%M:%S"),
                "state": "Known-Good Configuration Restored",
                "status": "RESTORED"
            }
        )

        st.rerun()

with button3:
    if st.button("🔍 Run Compliance Check", use_container_width=True):
        if (
            st.session_state.apache
            and st.session_state.port == 80
            and st.session_state.firewall
        ):
            st.session_state.status = "COMPLIANT"
        else:
            st.session_state.status = "NON-COMPLIANT"

        st.rerun()

st.divider()

st.subheader("📜 Configuration History")

for item in reversed(st.session_state.history):
    if item["status"] == "COMPLIANT":
        st.success(
            f"{item['time']} — {item['state']} — {item['status']}"
        )
    elif item["status"] == "NON-COMPLIANT":
        st.error(
            f"{item['time']} — {item['state']} — {item['status']}"
        )
    else:
        st.info(
            f"{item['time']} — {item['state']} — {item['status']}"
        )

st.divider()

st.subheader("🔁 Rudder Rollback Workflow")

workflow = """
1. Desired configuration is defined.
2. Rudder monitors the managed configuration.
3. Configuration drift occurs.
4. Rudder identifies NON-COMPLIANT state.
5. Previous known-good configuration is identified.
6. Rollback configuration is recommended.
7. Correct configuration is reapplied.
8. Compliance is verified.
"""

st.code(workflow)

st.caption(
    "Prototype implementation based on the Configuration Rollback Recommendation System workflow."
)

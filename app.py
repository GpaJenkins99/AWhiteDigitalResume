from pathlib import Path

import streamlit as st
from PIL import Image

# ----- PATH SETTING -----#
current_dir = Path(__file__).parent if "_file_" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file_PDF = current_dir / "assets" / "AWhiteJr resume 2026.docx.pdf"
resume_file_WD = current_dir / "assets" / "AWhiteJr AWhiteJr resume 2026.docx"
profile_pic = current_dir / "assets" / "profile-pic.png"

# ----- GENERAL SETTINGS -----
PAGE_TITLE = "Digital Resume | Adrian White Jr"
PAGE_ICON = ":⛩:"
NAME = "Adrian White Jr"
DESCRIPTION = """
US Army Soldier | Painter| Model | Aspiring software engineer 
"""
EMAIL = "adrianawhitejr@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/adrian-white-jr-83b389197/",
    "GitHub": "https://github.com/GpaJenkins99",
}
PROJECTS = {
    "🏆 3D Model- simulating 3D objects in python": " https://github.com/GpaJenkins99/3D-model ",
    "🏆 ChatBox- attempt in creating ChatGBT": "https://github.com/GpaJenkins99/chatbox-",
    "🏆 Top Down Game- voxel legend of zelda ": "https://github.com/GpaJenkins99/Top-Down-Game",
    "🏆 Space Game- First python game ": "https://github.com/GpaJenkins99/space-game-",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# ----- LOAD CSS, PDF &PROFILE PIC -----
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file_PDF, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# ----- HERO SECTION -----
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume PDF",
        data=PDFbyte,
        file_name=resume_file_PDF.name,
        mime="application/octet-stream",
    )
    st.download_button(
        label="📄 Download Resume WORD",
        data=PDFbyte,
        file_name=resume_file_WD.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# ----- SOCIAL LINKS -----
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# ----- EXPERIENCE & QUALIFICATIONS -----
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - ✔️CompTIA Security+ CE (August 2021 to August 2026)
    - ✔️Top Secret Clearance TS/SCI (CI polygraph) 
    """
)

# ----- SKILLS -----
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
     - Windows Server 2012-2022,- TCP/IP, - WAN,    - Java,                    - System Administration  - Nessus
     - Microsoft Office 365,    - DNS,    - VoIP,   - django,                  - Network Support        - Vcenter
     - AWS,                     - LAN,    - SCCM,   - Remote Access Software,  - Vsphear                - Splunk
     - Adobe Creative Suite,    - VPN,    - WSUS,   - Microsoft Exchange,      - VCS                    - Service Now
     - Active Directory,        - DHCP,   - Python, - PowerShell,              - Vrealize               - Flexeara 
    """
)

# ----- WORK HISTORY -----
st.write("#")
st.subheader("Work History")
st.write("---")

# ----- JOB 1 -----
st.write("🚧", "**Systems Engineer lvl III WHS | Akima Data Management**")
st.write("June 2025 to present")
st.write("Pentagon")
st.write(
    """
   - ► Mentor junior engineers and administrators on secure Windows operations in classified environments
   - ► Produce and maintain technical documentation, SOPs, diagrams, and recovery procedures appropriate for classified systems
   - ► Communicate system status, risks, and recommendations clearly to leadership while adhering to classification guidelines
   - ► Maintain high availability and mission-critical uptime for classified systems supporting operational requirements
   - ► Design and test backup, recovery, and disaster recovery solutions compliant with classified data handling policies
   - ► Conduct capacity planning and lifecycle management for Windows servers and supporting infrastructure
   - ► Execute change management in controlled environments with strict documentation and approval process
   - ► Implement and manage account access controls, privileged access, and least-privilege models in classified environments
   - ► Skilled in scripting languages, particularly PowerShell, for automation and task optimization.
   - ► Developed Python scripts to streamline task sequences, enhancing operational efficiency.
   - ► Perform patch management and vulnerability remediation using approved tools and processes in air-gapped or restricted networks
   - ► Support security audits, inspections, and accreditation activities (RMF, ATO support, POA&M remediation)
   - ► Monitor systems for security events and anomalies, coordinating with cybersecurity teams as required
   - ► Serve as senior engineer responsible for design, deployment, and sustainment of Windows-based systems within a SECRET-classified environment
   - ► Engineer and maintain secure Windows Server infrastructure (Active Directory, Group Policy, DNS, DHCP, PKI) in accordance with DoD and organizational security requirements
    """
)

# ----- JOB 1 -----
st.write("🚧", "**Lead Systems Engineer/ Architect ODNI | CACI**")
st.write("May 2024 to Febuary2025 ")
st.write("Tysons McLean VA")
st.write(
    """
    (new contract leaving Cognito Cyber Group)
   - ► stablished and managed production, testing, and development domains, ensuring seamless operations.
   - ► Implemented SCCM and orchestrated system updates to enhance performance and security.
   - ► Managed Secure Internet Protocol Router (SIPR) accounts through active directory administration.
   - ► Scheduled essential maintenance periods to minimize operational disruptions.
   - ► OCollaborated with cross-functional teams to define, document, and align system requirements with business objectives.
   - ► Possess extensive experience in Microsoft Systems Engineering, specializing in Windows platform operating systems (Windows 10 and Server 2016-2019).
   - ► Proficient in Windows Active Directory suite, including DNS, DFS, ADCS, and GPOs.
   - ► Demonstrated expertise in virtualization products such as VMware vSphere, ESXi, and vRealize Operations.
   - ► Skilled in scripting languages, particularly PowerShell, for automation and task optimization.
   - ► Developed Python scripts to streamline task sequences, enhancing operational efficiency.
   - ► Designed and executed innovative network solutions, optimizing existing networks to meet organizational objectives.
   - ► Provided robust support for network equipment, including routers, proxy servers, switches, WAN accelerators, DNS, and DHCP servers.
   - ► Managed, configured, and operated Linux servers, integrating them for maintenance testing.
   - ► Responsible for hands-on installation, administration, and patching of RHEL/CentOS and UNIX operating systems.
   - ► Installed and maintained server infrastructure device operating system software, ensuring seamless functionality across platforms. both Windows and Linux
   - ► Conducted comprehensive scans of computer networks and Domains, diagnosing connectivity issues and addressing network vulnerabilities to uphold security standards.
   - ► Collaborated seamlessly with cross-functional teams to define, document, and align system requirements with business objectives.
   - ► Worked closely with development teams to integrate Atlassian tools into workflows, providing guidance and support.
    """
)

# ----- JOB 1 -----
st.write("🚧", "**Lead Systems Engineer/ Architect ODNI | Cognito Cyber group**")
st.write("September 2023 to May 2024")
st.write("Tysons McLean VA")
st.write(
    """
   - ► stablished and managed production, testing, and development domains, ensuring seamless operations.
   - ► Implemented SCCM and orchestrated system updates to enhance performance and security.
   - ► Managed Secure Internet Protocol Router (SIPR) accounts through active directory administration.
   - ► Scheduled essential maintenance periods to minimize operational disruptions.
   - ► OCollaborated with cross-functional teams to define, document, and align system requirements with business objectives.
   - ► Possess extensive experience in Microsoft Systems Engineering, specializing in Windows platform operating systems (Windows 10 and Server 2016-2019).
   - ► Proficient in Windows Active Directory suite, including DNS, DFS, ADCS, and GPOs.
   - ► Demonstrated expertise in virtualization products such as VMware vSphere, ESXi, and vRealize Operations.
   - ► Skilled in scripting languages, particularly PowerShell, for automation and task optimization.
   - ► Developed Python scripts to streamline task sequences, enhancing operational efficiency.
   - ► Designed and executed innovative network solutions, optimizing existing networks to meet organizational objectives.
   - ► Provided robust support for network equipment, including routers, proxy servers, switches, WAN accelerators, DNS, and DHCP servers.
   - ► Managed, configured, and operated Linux servers, integrating them for maintenance testing.
   - ► Responsible for hands-on installation, administration, and patching of RHEL/CentOS and UNIX operating systems.
   - ► Installed and maintained server infrastructure device operating system software, ensuring seamless functionality across platforms. both Windows and Linux
   - ► Conducted comprehensive scans of computer networks and Domains, diagnosing connectivity issues and addressing network vulnerabilities to uphold security standards.
    """
)

# ----- JOB 1 -----
st.write("🚧", "**Systems Engineer MSTP | Obsidian Solutions Group**")
st.write("December 2022 to october 2023")
st.write("Quantico VA")
st.write(
    """
    (new contract leaving Innovative Reasoning)
   - ► Oversaw server statuses and operational functionality at a military training facility, ensuring seamless operations.
   - ► Applied critical maintenance patches and updates to enhance system performance and security.
   - ► Delivered comprehensive computer maintenance classes to marine personnel, contributing to their technical proficiency.
   - ► Strategically reimaged end user clients across the building infrastructure, optimizing user experiences. 
   - ► Orchestrated system updates and efficiently managed queues using SCCM and WSUS frameworks.
   - ► Provided adept back-end assistance to marines during rigorous training exercises, ensuring uninterrupted operations.
   - ► Skillfully managed Secure Internet Protocol Router (SIPR) accounts through active directory administration.
   - ► Scheduled essential maintenance periods for requisite updates, minimizing operational disruptions.
   - ► Monitored system performance and executed routine tuning and optimization initiatives to uphold efficiency.
   - ► Demonstrated expertise in engineering and maintaining shared corporate infrastructure.
   - ► Proficiently executed and supervised PowerShell scripts for image updates, enhancing system functionality.
   - ► Developed and programmed Python scripts to streamline task sequences, augmenting operational efficiency.
   - ► Collaborated seamlessly with cross-functional teams to define, document, and align system requirements with business objectives.
   - ► Worked closely with development teams to integrate Atlassian tools into workflows, providing guidance and support.
    """
)

# ----- JOB 2 -----
st.write("🚧", "**Systems Engineer MSTP | Innovative Reasoning**")
st.write("March 2022 to December 2022")
st.write("Quantico VA")
st.write(
    """
   - ► Oversaw server statuses and operational functionality at a military training facility, ensuring seamless operations.
   - ► Applied critical maintenance patches and updates to enhance system performance and security.
   - ► Delivered comprehensive computer maintenance classes to marine personnel, contributing to their technical proficiency.
   - ► Strategically reimaged end user clients across the building infrastructure, optimizing user experiences. 
   - ► Orchestrated system updates and efficiently managed queues using SCCM and WSUS frameworks.
   - ► Provided adept back-end assistance to marines during rigorous training exercises, ensuring uninterrupted operations.
   - ► Skillfully managed Secure Internet Protocol Router (SIPR) accounts through active directory administration.
   - ► Scheduled essential maintenance periods for requisite updates, minimizing operational disruptions.
   - ► Monitored system performance and executed routine tuning and optimization initiatives to uphold efficiency.
   - ► Demonstrated expertise in engineering and maintaining shared corporate infrastructure.
   - ► Proficiently executed and supervised PowerShell scripts for image updates, enhancing system functionality.
   - ► Developed and programmed Python scripts to streamline task sequences, augmenting operational efficiency.
   - ► Collaborated seamlessly with cross-functional teams to define, document, and align system requirements with business objectives.
   - ► Worked closely with development teams to integrate Atlassian tools into workflows, providing guidance and support.
    """
)

# ----- JOB 3 -----
st.write("🚧", "**System Administrator DIA | Vexterra**")
st.write("August 2021 to March 2022")
st.write("Reston, VA / Remote")
st.write(
    """
   - ► Provided adept engineering support for the design, configuration, and troubleshooting of both open source and commercial applications
   - ► sCollaborated seamlessly within the engineering team to enhance the supportability of systems, emphasizing improvements in backup and restoration processes
   - ► Offered comprehensive user support for systems, addressing queries and resolving technical issues promptly.
   - ► Produced meticulous documentation outlining system architecture, facilitating clear understanding and future maintenance
   - ► Developed comprehensive end-user documentation, enabling effective system utilization and troubleshooting.
   - ► Demonstrated proficiency in utilizing Docker and Kubernetes to manage cloud-based environments, optimizing efficiency and scalability.
    """
)

# ----- JOB 4 -----
st.write("🚧", "**Network Engineer HMX-1 | Greenfield Engineering**")
st.write("October 2020 to October 2021")
st.write("Quantico VA / PAX River Navy base")
st.write(
    """
   - ► Designed and executed novel network solutions, and enhanced the efficiency of existing networks to align with organizational objectives.
   - ► Installed, configured, and provided robust support for an array of network equipment, encompassing routers, proxy servers, switches, WAN accelerators, DNS, and DHCP servers.
   - ► Orchestrated the procurement of network equipment and expertly managed subcontractors engaged in network installation projects.
   - ► Skillfully configured firewalls, routing, and switching protocols to optimize network security and performance.
   - ► Monitored network health consistently, identifying and resolving issues to ensure peak performance and reliability.
   - ► Strategically planned and executed scheduled network upgrades, minimizing disruptions and enhancing capabilities. 
   - ► Conducted thorough investigations into network faults, swiftly resolving issues to maintain seamless operations.
   - ► Ensured network equipment was up-to-date with the latest firmware releases, enhancing security and functionality.
   - ► Delivered concise network status reports to key stakeholders, enabling informed decision-making.
   - ► Provided comprehensive training to marine personnel, empowering them with troubleshooting skills to resolve network-related challenges.
   - ► Collaborated effectively with communications equipment involving radio frequencies, contributing to seamless integration and operations.
    """
)

# ----- JOB 5 -----
st.write("🚧", "**Help Desk Technician NMCI | Super Systems Inc.**")
st.write("April 2019 to Sept 2020")
st.write("Norfolk, VA")
st.write(
    """
   - ► Leveraged strong problem-solving skills to provide effective assistance to customers in resolving technical issues.
   - ► Demonstrated proficiency in handling customer calls with professionalism and timeliness, ensuring high-quality service.
   - ► Provided expert guidance to customers facing challenges with CAC certificates, streamlining their access to secure systems.
   - ► Effectively managed, created, escalated, and concluded tickets utilizing HP Service Manager, maintaining meticulous records.
   - ► Orchestrated seamless installation and upkeep of personal computers and mainframe terminals, ensuring optimal functionality.
   - ► Efficiently accepted and managed work orders from customers, maintaining comprehensive daily operational logs.
   - ► Exhibited expertise in PC (desktop & laptop) upgrades, configuration, maintenance, troubleshooting, and repairs.
   - ► Employed remote access tools to deliver remote assistance to end-users, enhancing problem resolution efficiency.
   - ► Demonstrated proficiency in utilizing Microsoft Office 365 for effective communication and documentation.
   - ► Conducted weekly and monthly statistical analysis and metrics of helpdesk activities, contributing to performance evaluation.
   - ► Methodically documented technical issues reported by customers using Remedy, ensuring clear communication.
   - ► Maintained a professional demeanor and consistently delivered excellent customer service, fostering positive interactions.
   - ► Collaborated with end-users to facilitate password setup and user account activation, ensuring seamless access to systems.
    """
)

# ----- JOB 5 -----
st.write("🚧", "**Information Technology Specialist 5-159th HHC GSAB | U.S. Army Reserve.**")
st.write("December 2017 to December 2023")
st.write("Fort Eustis, VA")
st.write(
    """
   - ► Proficiently executes networking tasks on Cisco routers, encompassing activities such as port security clearance and user interface maintenance.
   - ► Offers adept technical support to field engineers, technicians, and military personnel, ensuring seamless operational continuity.
   - ► Demonstrates expertise in troubleshooting and resolving user issues, effectively tracking them using Remedy software. Responds promptly to user calls concerning technical matters related to workstations, printers, digital scanners, and VOIP phones.
   - ► Develops innovative solutions for a diverse range of challenges with a focus on moderate scope and complexity. Contributes actively to the achievement of organizational objectives and project completion.
   - ► Collaborates within a dedicated service team to achieve daily and monthly goals, consistently prioritizing customer satisfaction.
   - ► Conducts thorough analysis of outages and implements corrective actions, communicating findings and solutions to the Theater Network Operations Center.
   - ► Holds the crucial responsibility of ensuring continuous operation of Microsoft Exchange servers, which support essential software applications and databases critical to mission success.
    """
)

# ----- PROJECTS & ACCOMPLISHMENTS -----
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
    



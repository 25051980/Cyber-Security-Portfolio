# Penetration Testing & Vulnerability Assessment — Controlled Lab

## 📄 Full Technical Report

The complete MSc assessment report, including methodology, evidence, findings, mitigation and re-testing, is available here:

[View Full Penetration Testing Assessment Report](<CS07018 – Penetration Testing Engagement in a Controlled Lab (1).pdf>)

## Overview

This project demonstrates a structured penetration testing engagement conducted as part of my MSc in Computer Science with Cyber Security at St Mary's University, Twickenham.

The assessment was performed within an isolated and authorised GNS3 laboratory environment. The lab consisted of Kali Linux as the security testing workstation, Metasploitable2 as an intentionally vulnerable target server, and Ubuntu as a client system.

The objective was to identify exposed network services, research potential vulnerabilities, assess their security impact, document findings, implement mitigation measures, and verify remediation through re-testing.

## Lab Environment

The virtual network was created using GNS3 and included:

- Kali Linux — penetration testing workstation
- Metasploitable2 — intentionally vulnerable target
- Ubuntu Linux — client system
- Virtual network switch

All security testing was performed exclusively within the controlled academic environment.

## Penetration Testing Methodology

The assessment followed a structured workflow:

1. Lab configuration and connectivity verification
2. Network reconnaissance
3. Service scanning and enumeration
4. Vulnerability research
5. Vulnerability validation
6. Security impact analysis
7. Mitigation
8. Re-testing and evaluation

## Tools & Technologies

- Kali Linux
- GNS3
- Nmap
- Metasploit Framework
- SearchSploit
- Netcat
- Linux
- iptables
- Metasploitable2
- Ubuntu

## Network Reconnaissance & Enumeration

Network reconnaissance was conducted to identify accessible services and potential attack surfaces within the controlled environment.

Nmap service enumeration identified several exposed services on the intentionally vulnerable target, including FTP, database services, IRC, Apache Tomcat and an exposed root shell service.

The results were then analysed to identify services requiring further security investigation.

## Vulnerability Assessment

Vulnerability research was conducted against services identified during enumeration.

SearchSploit and the Metasploit Framework were used to investigate publicly documented vulnerabilities associated with identified software versions.

One of the principal findings involved a vulnerable UnrealIRCd service associated with a known backdoor command execution vulnerability.

## Security Findings

### Finding 1 — Vulnerable UnrealIRCd Service

Service enumeration identified an exposed UnrealIRCd service.

Further vulnerability research identified a known backdoor command execution vulnerability affecting the discovered version.

The finding demonstrated the security risks associated with running outdated or compromised software components.

Recommended mitigations included:

- upgrading or removing vulnerable software;
- restricting unnecessary network access;
- reducing exposed services;
- monitoring systems for suspicious activity.

### Finding 2 — Exposed Root Bindshell

A second significant finding involved an exposed bindshell service that permitted unauthenticated privileged access to the intentionally vulnerable target.

Testing within the isolated lab confirmed that the service represented a critical security risk because successful access could result in complete compromise of the affected system.

## Detection & Impact Analysis

Post-assessment analysis included examination of system activity and potential indicators of compromise.

The project considered evidence such as:

- network scanning activity;
- service enumeration;
- suspicious exposed services;
- privileged access;
- system login activity;
- running processes.

This stage demonstrated the relationship between offensive security testing and defensive detection and incident analysis.

## Mitigation & Re-Testing

A host-based firewall control was implemented to restrict access to the exposed vulnerable service.

The target was subsequently re-tested using Nmap. The previously accessible service was reported as filtered, demonstrating that the mitigation successfully prevented the tested form of remote access.

The assessment also recognised that mitigating a single vulnerability does not secure an intentionally vulnerable system and that additional patching, service reduction and system hardening would still be required.

## Skills Demonstrated

- Penetration Testing
- Vulnerability Assessment
- Network Reconnaissance
- Network Enumeration
- Vulnerability Research
- Linux
- Kali Linux
- Nmap
- Metasploit Framework
- SearchSploit
- Netcat
- GNS3
- Firewall Configuration
- Security Hardening
- Risk Assessment
- Security Documentation
- Remediation Testing

## Key Learning Outcomes

This project strengthened my practical understanding of the complete vulnerability management lifecycle — from identifying exposed services and researching vulnerabilities through security validation, impact analysis, remediation and re-testing.

It also reinforced the importance of clearly defined scope, rules of engagement, evidence collection and responsible security testing.

## Ethical & Legal Notice

All penetration testing activities documented in this project were performed within an isolated and authorised academic laboratory environment using intentionally vulnerable systems.

No testing was conducted against external, public or unauthorised systems.

This repository is intended solely to demonstrate cybersecurity knowledge, methodology and professional development.

# The Browser Security Model & Same-Origin Policy (SOP)

## Executive Summary

The **Same-Origin Policy (SOP)** is the fundamental security boundary of the web. It dictates that a web page from Origin A (`https://bank.com:443`) cannot read or access DOM elements, cookies, or fetch responses from Origin B (`https://evil.com:443`).

An Origin is defined strictly as the tuple:
$$\text{Origin} = \langle \text{Protocol}, \, \text{Host}, \, \text{Port} \rangle$$
Any deviation in any of the three elements constitutes a cross-origin boundary requiring explicit browser relaxation (via CORS).

---
title: AuthModerne
description: Streamlined authentication for modern Python applications
hide:
    - navigation
    - toc
---

<style>
.hero-wrapper {
    position: relative;
    text-align: center;
    margin: 3rem 0;
    padding: 2rem 0;
}

.hero-building-left,
.hero-building-right {
    position: absolute;
    bottom: -3rem;
    width: 280px;
    height: auto;
    opacity: 0.18;
    pointer-events: none;
}

.hero-building-left {
    left: 10px;
}

.hero-building-right {
    right: 10px;
}

[data-md-color-scheme="slate"] .hero-building-left,
[data-md-color-scheme="slate"] .hero-building-right {
    opacity: 0.12;
}

.hero-content {
    max-width: 600px;
    margin: 0 auto;
}

@media (max-width: 960px) {
    .hero-building-left,
    .hero-building-right {
        display: none;
    }
}
</style>

<div class="hero-wrapper">
    <!-- Left building caryatid -->
    <svg class="hero-building-left" viewBox="0 0 250 400" xmlns="http://www.w3.org/2000/svg">
        <g stroke="currentColor" fill="none" stroke-width="1.5">
            <!-- Far left background building - Art Deco style -->
            <g opacity="0.35">
                <rect x="0" y="150" width="50" height="250" rx="0"/>
                <line x1="0" y1="180" x2="50" y2="180"/>
                <line x1="0" y1="220" x2="50" y2="220"/>
                <line x1="0" y1="260" x2="50" y2="260"/>
                <line x1="0" y1="300" x2="50" y2="300"/>
                <line x1="0" y1="340" x2="50" y2="340"/>
                <line x1="0" y1="380" x2="50" y2="380"/>
                <!-- Stepped ziggurat top -->
                <rect x="10" y="130" width="30" height="20"/>
                <rect x="15" y="115" width="20" height="15"/>
                <line x1="15" y1="150" x2="15" y2="400"/>
                <line x1="35" y1="150" x2="35" y2="400"/>
            </g>

            <!-- Mid-left shorter building with rounded top -->
            <g opacity="0.45">
                <rect x="45" y="200" width="40" height="200" rx="0"/>
                <line x1="45" y1="230" x2="85" y2="230"/>
                <line x1="45" y1="270" x2="85" y2="270"/>
                <line x1="45" y1="310" x2="85" y2="310"/>
                <line x1="45" y1="350" x2="85" y2="350"/>
                <!-- Wide rounded cap -->
                <path d="M 40 200 L 40 185 Q 65 175 90 185 L 90 200 Z"/>
                <circle cx="65" cy="180" r="3" fill="currentColor"/>
            </g>

            <!-- Background building (right side, behind main tower) - different style -->
            <g opacity="0.5">
                <rect x="180" y="120" width="50" height="280" rx="0"/>
                <line x1="180" y1="150" x2="230" y2="150"/>
                <line x1="180" y1="190" x2="230" y2="190"/>
                <line x1="180" y1="230" x2="230" y2="230"/>
                <line x1="180" y1="270" x2="230" y2="270"/>
                <line x1="180" y1="310" x2="230" y2="310"/>
                <line x1="180" y1="350" x2="230" y2="350"/>
                <!-- Square crown with antenna -->
                <rect x="185" y="100" width="40" height="20"/>
                <rect x="200" y="90" width="10" height="10"/>
                <line x1="205" y1="90" x2="205" y2="75"/>
                <circle cx="205" cy="72" r="3" fill="currentColor"/>
                <!-- Vertical divider -->
                <line x1="205" y1="120" x2="205" y2="400"/>
            </g>

            <!-- Far right partial building -->
            <g opacity="0.4">
                <rect x="225" y="180" width="25" height="220" rx="0"/>
                <line x1="225" y1="210" x2="250" y2="210"/>
                <line x1="225" y1="250" x2="250" y2="250"/>
                <line x1="225" y1="290" x2="250" y2="290"/>
                <line x1="225" y1="330" x2="250" y2="330"/>
                <line x1="225" y1="370" x2="250" y2="370"/>
            </g>

            <!-- Main tower structure -->
            <rect x="90" y="30" width="100" height="370" rx="0"/>

            <!-- Stepped top detail -->
            <rect x="100" y="15" width="80" height="15"/>
            <rect x="115" y="5" width="50" height="10" rx="5"/>
            <circle cx="140" cy="3" r="3" fill="currentColor"/>

            <!-- Horizontal window bands -->
            <line x1="90" y1="60" x2="190" y2="60"/>
            <line x1="90" y1="90" x2="190" y2="90"/>
            <line x1="90" y1="120" x2="190" y2="120"/>
            <line x1="90" y1="150" x2="190" y2="150"/>
            <line x1="90" y1="180" x2="190" y2="180"/>
            <line x1="90" y1="210" x2="190" y2="210"/>
            <line x1="90" y1="240" x2="190" y2="240"/>
            <line x1="90" y1="270" x2="190" y2="270"/>
            <line x1="90" y1="300" x2="190" y2="300"/>
            <line x1="90" y1="330" x2="190" y2="330"/>
            <line x1="90" y1="360" x2="190" y2="360"/>

            <!-- Vertical divisions creating window grid -->
            <line x1="115" y1="30" x2="115" y2="400"/>
            <line x1="140" y1="30" x2="140" y2="400"/>
            <line x1="165" y1="30" x2="165" y2="400"/>

            <!-- Decorative vertical strips -->
            <rect x="95" y="30" width="3" height="370" fill="currentColor" opacity="0.3"/>
            <rect x="182" y="30" width="3" height="370" fill="currentColor" opacity="0.3"/>

            <!-- Base detail -->
            <rect x="0" y="395" width="250" height="5" fill="currentColor" opacity="0.2"/>
        </g>
    </svg>
    <!-- Center hero content -->
    <div class="hero-content">
        <h1>AuthModerne</h1>
        <p><strong>Streamlined authentication for modern Python applications.</strong></p>
        <p>
            <a href="#installation" class="md-button md-button--primary">Get Started</a>
            <a href="https://github.com/frankie567/authmoderne" class="md-button">View on GitHub</a>
        </p>
    </div>

    <!-- Right building caryatid -->
    <svg class="hero-building-right" viewBox="0 0 280 400" xmlns="http://www.w3.org/2000/svg">
        <g stroke="currentColor" fill="none" stroke-width="1.5">
            <!-- Far left partial building - slim tower -->
            <g opacity="0.35">
                <rect x="0" y="170" width="30" height="230" rx="0"/>
                <line x1="0" y1="200" x2="30" y2="200"/>
                <line x1="0" y1="240" x2="30" y2="240"/>
                <line x1="0" y1="280" x2="30" y2="280"/>
                <line x1="0" y1="320" x2="30" y2="320"/>
                <line x1="0" y1="360" x2="30" y2="360"/>
                <rect x="5" y="155" width="20" height="15" rx="7"/>
            </g>

            <!-- Left background tower - taller with horizontal emphasis -->
            <g opacity="0.45">
                <rect x="25" y="100" width="45" height="300" rx="0"/>
                <line x1="25" y1="130" x2="70" y2="130"/>
                <line x1="25" y1="170" x2="70" y2="170"/>
                <line x1="25" y1="210" x2="70" y2="210"/>
                <line x1="25" y1="250" x2="70" y2="250"/>
                <line x1="25" y1="290" x2="70" y2="290"/>
                <line x1="25" y1="330" x2="70" y2="330"/>
                <line x1="25" y1="370" x2="70" y2="370"/>
                <!-- Flat rectangular top -->
                <rect x="30" y="80" width="35" height="20"/>
                <rect x="37" y="70" width="21" height="10"/>
                <line x1="47" y1="100" x2="47" y2="400"/>
            </g>

            <!-- Right background - wide low building -->
            <g opacity="0.4">
                <rect x="225" y="190" width="55" height="210" rx="0"/>
                <line x1="225" y1="220" x2="280" y2="220"/>
                <line x1="225" y1="260" x2="280" y2="260"/>
                <line x1="225" y1="300" x2="280" y2="300"/>
                <line x1="225" y1="340" x2="280" y2="340"/>
                <line x1="225" y1="380" x2="280" y2="380"/>
                <!-- Curved top element -->
                <path d="M 230 190 L 230 180 Q 252 170 275 180 L 275 190" fill="none"/>
                <line x1="245" y1="190" x2="245" y2="400"/>
                <line x1="260" y1="190" x2="260" y2="400"/>
            </g>

            <!-- Far right edge building -->
            <g opacity="0.35">
                <rect x="270" y="230" width="10" height="170" rx="0"/>
                <line x1="270" y1="260" x2="280" y2="260"/>
                <line x1="270" y1="300" x2="280" y2="300"/>
                <line x1="270" y1="340" x2="280" y2="340"/>
                <line x1="270" y1="380" x2="280" y2="380"/>
            </g>

            <!-- Wide horizontal base structure -->
            <rect x="70" y="70" width="160" height="330" rx="0"/>

            <!-- Curved corner detail (signature Streamline Moderne) -->
            <path d="M 230 90 Q 230 70 210 70" fill="none"/>

            <!-- Stepped tower element -->
            <rect x="120" y="30" width="70" height="40"/>
            <rect x="135" y="15" width="40" height="15" rx="7"/>
            <circle cx="155" cy="10" r="4" fill="currentColor"/>

            <!-- Horizontal bands emphasizing width -->
            <line x1="70" y1="100" x2="230" y2="100"/>
            <line x1="70" y1="130" x2="230" y2="130"/>
            <line x1="70" y1="160" x2="230" y2="160"/>
            <line x1="70" y1="190" x2="230" y2="190"/>
            <line x1="70" y1="220" x2="230" y2="220"/>
            <line x1="70" y1="250" x2="230" y2="250"/>
            <line x1="70" y1="280" x2="230" y2="280"/>
            <line x1="70" y1="310" x2="230" y2="310"/>
            <line x1="70" y1="340" x2="230" y2="340"/>
            <line x1="70" y1="370" x2="230" y2="370"/>

            <!-- Vertical window strips -->
            <line x1="110" y1="70" x2="110" y2="400"/>
            <line x1="155" y1="30" x2="155" y2="400"/>
            <line x1="200" y1="70" x2="200" y2="400"/>

            <!-- Circular porthole window with details -->
            <circle cx="155" cy="220" r="35"/>
            <circle cx="155" cy="220" r="26"/>
            <circle cx="155" cy="220" r="17"/>
            <circle cx="155" cy="220" r="8" fill="currentColor" opacity="0.3"/>

            <!-- Porthole cross divisions -->
            <line x1="155" y1="185" x2="155" y2="255" opacity="0.5"/>
            <line x1="120" y1="220" x2="190" y2="220" opacity="0.5"/>

            <!-- Decorative speed lines on right -->
            <line x1="210" y1="90" x2="225" y2="90" stroke-width="2"/>
            <line x1="210" y1="150" x2="225" y2="150" stroke-width="2"/>
            <line x1="210" y1="260" x2="225" y2="260" stroke-width="2"/>
            <line x1="210" y1="320" x2="225" y2="320" stroke-width="2"/>

            <!-- Base platform -->
            <rect x="0" y="395" width="280" height="5" fill="currentColor" opacity="0.2"/>

            <!-- Vertical accent strips -->
            <rect x="75" y="70" width="3" height="330" fill="currentColor" opacity="0.3"/>
            <rect x="222" y="70" width="3" height="330" fill="currentColor" opacity="0.3"/>
        </g>
    </svg>

</div>

---

## Features

<div class="grid cards" markdown>

- :material-lightning-bolt:{ .lg .middle } **Fast & Efficient**

    ***

    Built for performance with modern async Python, AuthModerne handles authentication without slowing down your application.

- :material-puzzle:{ .lg .middle } **Modular Design**

    ***

    Pick and choose the components you need. Clean, composable architecture inspired by Streamline Moderne principles.

- :material-shield-check:{ .lg .middle } **Secure by Default**

    ***

    Industry-standard security practices built-in. Focus on your application, not security edge cases.

- :material-code-braces:{ .lg .middle } **Developer Friendly**

    ***

    Intuitive API with full type hints and comprehensive documentation. Get up and running in minutes.

- :material-cog:{ .lg .middle } **Highly Configurable**

    ***

    Flexible configuration options to match your exact requirements without unnecessary complexity.

- :material-update:{ .lg .middle } **Modern Python**

    ***

    Built with the latest Python features and best practices for clean, maintainable code.

</div>

---

## Installation

Get started with AuthModerne in seconds:

```bash
pip install authmoderne
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add authmoderne
```

---

## Quick Start

<div class="grid" markdown>

!!! example "Basic Usage"

    ```python
    # TODO
    ```

!!! tip "Configuration"

    ```python
    # TODO
    ```

</div>

---

## Why AuthModerne?

AuthModerne brings the elegance of **Streamline Moderne** design principles to Python authentication:

- **Clean lines** - Simple, composable API without unnecessary complexity
- **Functional beauty** - Every component serves a purpose
- **Modern approach** - Built for contemporary Python applications

Just like the Art Deco movement emphasized sleek, horizontal lines and minimal ornamentation, AuthModerne focuses on essential functionality delivered with style.

---

## Next Steps

<div class="grid cards" markdown>

- :material-book-open-variant:{ .lg .middle } **Documentation**

    ***

    Explore the complete API reference and detailed guides

    [:octicons-arrow-right-24: API Reference](reference/authmoderne.md)

- :material-github:{ .lg .middle } **Source Code**

    ***

    Contribute to the project or report issues on GitHub

    [:octicons-arrow-right-24: GitHub Repository](https://github.com/frankie567/authmoderne)

- :material-file-document:{ .lg .middle } **License**

    ***

    AuthModerne is open source under the MIT License

    [:octicons-arrow-right-24: MIT License](https://github.com/frankie567/authmoderne/blob/master/LICENSE)

</div>

---

<div style="text-align: center; margin: 3rem 0; opacity: 0.7;" markdown>

Made with :material-train-variant: by the AuthModerne team

</div>

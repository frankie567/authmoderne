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
    width: 180px;
    height: auto;
    opacity: 0.18;
    pointer-events: none;
}

.hero-building-left {
    left: 20px;
}

.hero-building-right {
    right: 20px;
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
    <svg class="hero-building-left" viewBox="0 0 140 400" xmlns="http://www.w3.org/2000/svg">
        <g stroke="currentColor" fill="none" stroke-width="1.5">
            <!-- Main tower structure -->
            <rect x="20" y="40" width="100" height="360" rx="0"/>

            <!-- Stepped top detail -->
            <rect x="30" y="25" width="80" height="15"/>
            <rect x="45" y="15" width="50" height="10" rx="5"/>
            <circle cx="70" cy="10" r="3" fill="currentColor"/>

            <!-- Horizontal window bands -->
            <line x1="20" y1="70" x2="120" y2="70"/>
            <line x1="20" y1="100" x2="120" y2="100"/>
            <line x1="20" y1="130" x2="120" y2="130"/>
            <line x1="20" y1="160" x2="120" y2="160"/>
            <line x1="20" y1="190" x2="120" y2="190"/>
            <line x1="20" y1="220" x2="120" y2="220"/>
            <line x1="20" y1="250" x2="120" y2="250"/>
            <line x1="20" y1="280" x2="120" y2="280"/>
            <line x1="20" y1="310" x2="120" y2="310"/>
            <line x1="20" y1="340" x2="120" y2="340"/>
            <line x1="20" y1="370" x2="120" y2="370"/>

            <!-- Vertical divisions creating window grid -->
            <line x1="45" y1="40" x2="45" y2="400"/>
            <line x1="70" y1="40" x2="70" y2="400"/>
            <line x1="95" y1="40" x2="95" y2="400"/>

            <!-- Decorative vertical strips -->
            <rect x="25" y="40" width="3" height="360" fill="currentColor" opacity="0.3"/>
            <rect x="112" y="40" width="3" height="360" fill="currentColor" opacity="0.3"/>

            <!-- Base detail -->
            <rect x="15" y="395" width="110" height="5" fill="currentColor" opacity="0.2"/>
        </g>
    </svg>
    <!-- Center hero content -->
    <div class="hero-content">
        <h1>AuthModerne</h1>
        <p><strong>Streamlined authentication for modern Python applications.</strong></p>
        <p>
            <a href="https://github.com/frankie567/authmoderne/actions"><img src="https://github.com/frankie567/authmoderne/workflows/Build/badge.svg" alt="build"></a>
            <a href="https://codecov.io/gh/frankie567/authmoderne"><img src="https://codecov.io/gh/frankie567/authmoderne/branch/master/graph/badge.svg" alt="codecov"></a>
            <a href="https://badge.fury.io/py/authmoderne"><img src="https://badge.fury.io/py/authmoderne.svg" alt="PyPI version"></a>
        </p>
        <p>
            <a href="#installation" class="md-button md-button--primary">Get Started</a>
            <a href="https://github.com/frankie567/authmoderne" class="md-button">View on GitHub</a>
        </p>
    </div>

    <!-- Right building caryatid -->
    <svg class="hero-building-right" viewBox="0 0 160 400" xmlns="http://www.w3.org/2000/svg">
        <g stroke="currentColor" fill="none" stroke-width="1.5">
            <!-- Wide horizontal base structure -->
            <rect x="10" y="80" width="140" height="320" rx="0"/>

            <!-- Curved corner detail (signature Streamline Moderne) -->
            <path d="M 150 100 Q 150 80 135 80" fill="none"/>

            <!-- Stepped tower element -->
            <rect x="50" y="40" width="60" height="40"/>
            <rect x="65" y="25" width="30" height="15" rx="7"/>
            <circle cx="80" cy="20" r="4" fill="currentColor"/>

            <!-- Horizontal bands emphasizing width -->
            <line x1="10" y1="110" x2="150" y2="110"/>
            <line x1="10" y1="140" x2="150" y2="140"/>
            <line x1="10" y1="170" x2="150" y2="170"/>
            <line x1="10" y1="200" x2="150" y2="200"/>
            <line x1="10" y1="230" x2="150" y2="230"/>
            <line x1="10" y1="260" x2="150" y2="260"/>
            <line x1="10" y1="290" x2="150" y2="290"/>
            <line x1="10" y1="320" x2="150" y2="320"/>
            <line x1="10" y1="350" x2="150" y2="350"/>
            <line x1="10" y1="380" x2="150" y2="380"/>

            <!-- Vertical window strips -->
            <line x1="40" y1="80" x2="40" y2="400"/>
            <line x1="80" y1="40" x2="80" y2="400"/>
            <line x1="120" y1="80" x2="120" y2="400"/>

            <!-- Circular porthole window with details -->
            <circle cx="80" cy="200" r="30"/>
            <circle cx="80" cy="200" r="22"/>
            <circle cx="80" cy="200" r="14"/>
            <circle cx="80" cy="200" r="6" fill="currentColor" opacity="0.3"/>

            <!-- Porthole cross divisions -->
            <line x1="80" y1="170" x2="80" y2="230" opacity="0.5"/>
            <line x1="50" y1="200" x2="110" y2="200" opacity="0.5"/>

            <!-- Decorative speed lines on right -->
            <line x1="130" y1="100" x2="145" y2="100" stroke-width="2"/>
            <line x1="130" y1="150" x2="145" y2="150" stroke-width="2"/>
            <line x1="130" y1="250" x2="145" y2="250" stroke-width="2"/>
            <line x1="130" y1="300" x2="145" y2="300" stroke-width="2"/>

            <!-- Base platform -->
            <rect x="5" y="395" width="150" height="5" fill="currentColor" opacity="0.2"/>

            <!-- Vertical accent strips -->
            <rect x="15" y="80" width="3" height="320" fill="currentColor" opacity="0.3"/>
            <rect x="142" y="80" width="3" height="320" fill="currentColor" opacity="0.3"/>
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
    from authmoderne import Auth

    # Initialize authentication
    auth = Auth()

    # Your authentication logic here
    @auth.login
    async def authenticate(username: str, password: str):
        # Verify credentials
        return user
    ```

!!! tip "Configuration"

    ```python
    from authmoderne import Config

    # Customize your setup
    config = Config(
        secret_key="your-secret-key",
        algorithm="HS256",
        token_expiry=3600
    )

    auth = Auth(config=config)
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

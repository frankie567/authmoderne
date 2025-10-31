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

.hero-buildings {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 100%;
    max-width: 1200px;
    height: auto;
    opacity: 0.08;
    pointer-events: none;
    z-index: 0;
}

[data-md-color-scheme="slate"] .hero-buildings {
    opacity: 0.06;
}

.hero-content {
    position: relative;
    z-index: 1;
}
</style>

<div class="hero-wrapper">
    <svg class="hero-buildings" viewBox="0 0 1200 400" xmlns="http://www.w3.org/2000/svg">
        <!-- Left building - tall with horizontal bands -->
        <g stroke="currentColor" fill="none" stroke-width="2">
            <!-- Main tower -->
            <rect x="50" y="120" width="120" height="280" rx="0"/>
            <!-- Horizontal bands -->
            <line x1="50" y1="160" x2="170" y2="160"/>
            <line x1="50" y1="200" x2="170" y2="200"/>
            <line x1="50" y1="240" x2="170" y2="240"/>
            <line x1="50" y1="280" x2="170" y2="280"/>
            <line x1="50" y1="320" x2="170" y2="320"/>
            <line x1="50" y1="360" x2="170" y2="360"/>
            <!-- Top detail -->
            <rect x="70" y="100" width="80" height="20" rx="10"/>
        </g>
        <!-- Center building - wide with curved corner -->
        <g stroke="currentColor" fill="none" stroke-width="2">
            <!-- Main structure -->
            <path d="M 250 180 L 250 400 L 550 400 L 550 200 Q 550 180 530 180 Z"/>
            <!-- Horizontal window bands -->
            <line x1="250" y1="220" x2="550" y2="220"/>
            <line x1="250" y1="260" x2="550" y2="260"/>
            <line x1="250" y1="300" x2="550" y2="300"/>
            <line x1="250" y1="340" x2="550" y2="340"/>
            <!-- Vertical divisions -->
            <line x1="320" y1="180" x2="320" y2="400"/>
            <line x1="400" y1="180" x2="400" y2="400"/>
            <line x1="480" y1="180" x2="480" y2="400"/>
            <!-- Stepped top -->
            <rect x="280" y="160" width="60" height="20"/>
            <rect x="360" y="140" width="60" height="20"/>
        </g>
        <!-- Right building - streamlined with porthole -->
        <g stroke="currentColor" fill="none" stroke-width="2">
            <!-- Main structure with rounded end -->
            <rect x="650" y="150" width="180" height="250" rx="0"/>
            <circle cx="830" cy="275" r="90"/>
            <!-- Horizontal speed lines -->
            <line x1="650" y1="190" x2="920" y2="190"/>
            <line x1="650" y1="230" x2="920" y2="230"/>
            <line x1="650" y1="270" x2="920" y2="270"/>
            <line x1="650" y1="310" x2="920" y2="310"/>
            <line x1="650" y1="350" x2="920" y2="350"/>
            <!-- Porthole window -->
            <circle cx="830" cy="275" r="35"/>
            <circle cx="830" cy="275" r="25"/>
        </g>
        <!-- Far right - small tower accent -->
        <g stroke="currentColor" fill="none" stroke-width="2">
            <rect x="1000" y="220" width="80" height="180" rx="0"/>
            <rect x="1015" y="200" width="50" height="20" rx="10"/>
            <line x1="1000" y1="260" x2="1080" y2="260"/>
            <line x1="1000" y1="300" x2="1080" y2="300"/>
            <line x1="1000" y1="340" x2="1080" y2="340"/>
        </g>
    </svg>
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

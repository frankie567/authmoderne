---
title: Authmoderne
description: Streamlined authentication for modern Python applications
hide:
    - navigation
    - toc
---

<style>
.hero-wrapper {
    position: relative;
    text-align: center;
    margin: 3rem 0 4rem 0;
    padding: 2rem 0;
}

.hero-skyline {
    position: absolute;
    bottom: -3rem;
    left: 50%;
    transform: translateX(-50%);
    width: 100%;
    max-width: 1200px;
    height: auto;
    pointer-events: none;
}

/* Greyish tones for buildings */
[data-md-color-scheme="default"] .hero-skyline {
    opacity: 0.3;
}

[data-md-color-scheme="slate"] .hero-skyline {
    opacity: 0.22;
}

.hero-content {
    position: relative;
    z-index: 1;
    max-width: 600px;
    margin: 0 auto 2rem auto;
}

@media (max-width: 960px) {
    .hero-skyline {
        display: none;
    }
}

.coming-soon-badge {
    display: inline-block;
    background: transparent;
    color: var(--md-primary-fg-color);
    border: 2px solid var(--md-primary-fg-color);
    padding: 0.5rem 1.5rem;
    border-radius: 2rem;
    font-weight: bold;
    font-size: 1.1em;
    margin: 0 0 0.75rem 0;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    font-size: 0.9em;
}

.hero-catchline {
    font-size: 1.3em;
    margin: 0.5rem 0 1.5rem 0;
}

.cta-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: nowrap;
    margin: 0;
}

.cta-buttons .md-button {
    white-space: nowrap;
}

@media (max-width: 760px) {
    .cta-buttons {
        flex-direction: column;
        align-items: stretch;
    }
}

/* Vision Section Styles */
.vision-section {
    max-width: 1000px;
    margin: 4rem auto;
    padding: 0 2rem;
}

.vision-hero {
    text-align: center;
    margin-bottom: 4rem;
}

.vision-hero h2 {
    font-size: 2.5em;
    font-weight: 700;
    margin-bottom: 1.5rem;
    line-height: 1.2;
}

.vision-tagline {
    font-size: 1.3em;
    color: var(--md-default-fg-color--light);
    max-width: 700px;
    margin: 0 auto;
    line-height: 1.6;
}

.problem-statement {
    background: var(--md-code-bg-color);
    border-radius: 12px;
    padding: 3rem 2.5rem;
    margin: 3rem 0;
    text-align: center;
}

.problem-statement h3 {
    font-size: 1.8em;
    margin-top: 0;
    margin-bottom: 1.5rem;
    font-weight: 600;
}

.problem-statement p {
    font-size: 1.2em;
    line-height: 1.7;
    margin: 1rem 0;
}

.principle-callout {
    background: linear-gradient(135deg, var(--md-primary-fg-color) 0%, var(--md-accent-fg-color) 100%);
    color: white;
    border-radius: 12px;
    padding: 2.5rem;
    margin: 3rem 0;
    text-align: center;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}

.principle-callout p {
    font-size: 1.5em;
    font-weight: 600;
    margin: 0;
    line-height: 1.4;
}

.features-intro {
    text-align: center;
    margin: 4rem 0 3rem 0;
}

.features-intro h3 {
    font-size: 2em;
    margin-bottom: 1rem;
    font-weight: 600;
}

.features-intro p {
    font-size: 1.2em;
    color: var(--md-default-fg-color--light);
    max-width: 650px;
    margin: 0 auto;
}

@media (max-width: 960px) {
    .vision-hero h2 {
        font-size: 2em;
    }

    .vision-tagline {
        font-size: 1.1em;
    }

    .problem-statement h3 {
        font-size: 1.5em;
    }

    .problem-statement p {
        font-size: 1.1em;
    }

    .principle-callout p {
        font-size: 1.3em;
    }

    .features-intro h3 {
        font-size: 1.6em;
    }
}
</style>

<div class="hero-wrapper">
    <!-- Skyline backdrop -->
    <svg class="hero-skyline" viewBox="0 0 1200 301" xmlns="http://www.w3.org/2000/svg">
        <g stroke="currentColor" stroke-width="1.8">
            <!-- Ground line -->
            <line x1="0" y1="300" x2="1200" y2="300" stroke-width="1.8" opacity="0.5"/>

            <!-- LEFT SIDE - Tall Buildings (back to front) -->

            <!-- Far back left building -->
            <g opacity="0.5">
                <rect x="55" y="100" width="45" height="200" rx="0" fill="currentColor" opacity="0.2"/>
                <rect x="55" y="100" width="45" height="200" rx="0" fill="none"/>
                <rect x="62" y="85" width="31" height="15" fill="currentColor" opacity="0.2"/>
                <rect x="62" y="85" width="31" height="15" fill="none"/>
                <line x1="55" y1="130" x2="100" y2="130"/>
                <line x1="55" y1="165" x2="100" y2="165"/>
                <line x1="55" y1="200" x2="100" y2="200"/>
                <line x1="55" y1="235" x2="100" y2="235"/>
                <line x1="55" y1="270" x2="100" y2="270"/>
                <line x1="77" y1="100" x2="77" y2="300"/>
            </g>

            <!-- Middle left building - Art Deco ziggurat -->
            <g opacity="0.65">
                <rect x="120" y="120" width="55" height="180" rx="0" fill="currentColor" opacity="0.3"/>
                <rect x="120" y="120" width="55" height="180" rx="0" fill="none"/>
                <rect x="127" y="105" width="41" height="15" fill="currentColor" opacity="0.3"/>
                <rect x="127" y="105" width="41" height="15" fill="none"/>
                <rect x="135" y="92" width="25" height="13" fill="currentColor" opacity="0.3"/>
                <rect x="135" y="92" width="25" height="13" fill="none"/>
                <path d="M 130 120 L 130 105 Q 147 98 165 105 L 165 120 Z" fill="currentColor" opacity="0.3"/>
                <path d="M 130 120 L 130 105 Q 147 98 165 105 L 165 120 Z" fill="none"/>
                <circle cx="147" cy="100" r="2.5" fill="currentColor"/>
                <line x1="120" y1="145" x2="175" y2="145"/>
                <line x1="120" y1="175" x2="175" y2="175"/>
                <line x1="120" y1="205" x2="175" y2="205"/>
                <line x1="120" y1="235" x2="175" y2="235"/>
                <line x1="120" y1="265" x2="175" y2="265"/>
                <line x1="147" y1="120" x2="147" y2="300"/>
            </g>

            <!-- Front left tallest tower -->
            <g opacity="0.85">
                <rect x="0" y="40" width="80" height="260" rx="0" fill="currentColor" opacity="0.4"/>
                <rect x="0" y="40" width="80" height="260" rx="0" fill="none"/>
                <rect x="10" y="25" width="60" height="15" fill="currentColor" opacity="0.4"/>
                <rect x="10" y="25" width="60" height="15" fill="none"/>
                <rect x="25" y="15" width="30" height="10" rx="5" fill="currentColor" opacity="0.4"/>
                <rect x="25" y="15" width="30" height="10" rx="5" fill="none"/>
                <circle cx="40" cy="10" r="4" fill="currentColor"/>
                <line x1="0" y1="70" x2="80" y2="70"/>
                <line x1="0" y1="100" x2="80" y2="100"/>
                <line x1="0" y1="130" x2="80" y2="130"/>
                <line x1="0" y1="160" x2="80" y2="160"/>
                <line x1="0" y1="190" x2="80" y2="190"/>
                <line x1="0" y1="220" x2="80" y2="220"/>
                <line x1="0" y1="250" x2="80" y2="250"/>
                <line x1="0" y1="280" x2="80" y2="280"/>
                <line x1="27" y1="40" x2="27" y2="300"/>
                <line x1="53" y1="40" x2="53" y2="300"/>
                <rect x="5" y="40" width="3" height="260" fill="currentColor" opacity="0.45"/>
            </g>

            <!-- CENTER - Smaller Buildings (valley for hero text) -->

            <!-- Center left - medium building -->
            <g opacity="0.5">
                <rect x="350" y="185" width="55" height="115" rx="0" fill="currentColor" opacity="0.22"/>
                <rect x="350" y="185" width="55" height="115" rx="0" fill="none"/>
                <line x1="350" y1="210" x2="405" y2="210"/>
                <line x1="350" y1="240" x2="405" y2="240"/>
                <line x1="350" y1="270" x2="405" y2="270"/>
                <line x1="377" y1="185" x2="377" y2="300"/>
            </g>

            <!-- Center left-mid - slim tower -->
            <g opacity="0.4">
                <rect x="425" y="215" width="40" height="85" rx="0" fill="currentColor" opacity="0.18"/>
                <rect x="425" y="215" width="40" height="85" rx="0" fill="none"/>
                <rect x="431" y="205" width="28" height="10" rx="5" fill="currentColor" opacity="0.18"/>
                <rect x="431" y="205" width="28" height="10" rx="5" fill="none"/>
                <line x1="425" y1="240" x2="465" y2="240"/>
                <line x1="425" y1="270" x2="465" y2="270"/>
                <line x1="445" y1="215" x2="445" y2="300"/>
            </g>

            <!-- Center middle - tiny rounded building -->
            <g opacity="0.35">
                <rect x="485" y="235" width="38" height="65" rx="0" fill="currentColor" opacity="0.16"/>
                <rect x="485" y="235" width="38" height="65" rx="0" fill="none"/>
                <path d="M 490 235 L 490 228 Q 504 223 518 228 L 518 235 Z" fill="currentColor" opacity="0.16"/>
                <path d="M 490 235 L 490 228 Q 504 223 518 228 L 518 235 Z" fill="none"/>
                <circle cx="504" cy="225" r="2" fill="currentColor"/>
                <line x1="485" y1="258" x2="523" y2="258"/>
                <line x1="485" y1="280" x2="523" y2="280"/>
                <line x1="504" y1="235" x2="504" y2="300"/>
            </g>

            <!-- Center middle - wide low building -->
            <g opacity="0.38">
                <rect x="543" y="240" width="60" height="60" rx="0" fill="currentColor" opacity="0.17"/>
                <rect x="543" y="240" width="60" height="60" rx="0" fill="none"/>
                <line x1="543" y1="260" x2="603" y2="260"/>
                <line x1="543" y1="280" x2="603" y2="280"/>
                <line x1="563" y1="240" x2="563" y2="300"/>
                <line x1="583" y1="240" x2="583" y2="300"/>
            </g>

            <!-- Center middle-right - art deco style -->
            <g opacity="0.42">
                <rect x="623" y="220" width="50" height="80" rx="0" fill="currentColor" opacity="0.19"/>
                <rect x="623" y="220" width="50" height="80" rx="0" fill="none"/>
                <rect x="630" y="210" width="36" height="10" fill="currentColor" opacity="0.19"/>
                <rect x="630" y="210" width="36" height="10" fill="none"/>
                <rect x="638" y="202" width="20" height="8" fill="currentColor" opacity="0.19"/>
                <rect x="638" y="202" width="20" height="8" fill="none"/>
                <line x1="623" y1="244" x2="673" y2="244"/>
                <line x1="623" y1="272" x2="673" y2="272"/>
                <line x1="648" y1="220" x2="648" y2="300"/>
            </g>

            <!-- Center right-mid - narrow tower -->
            <g opacity="0.4">
                <rect x="693" y="210" width="42" height="90" rx="0" fill="currentColor" opacity="0.18"/>
                <rect x="693" y="210" width="42" height="90" rx="0" fill="none"/>
                <line x1="693" y1="235" x2="735" y2="235"/>
                <line x1="693" y1="265" x2="735" y2="265"/>
                <line x1="714" y1="210" x2="714" y2="300"/>
            </g>

            <!-- Center far right - medium building -->
            <g opacity="0.47">
                <rect x="755" y="195" width="55" height="105" rx="0" fill="currentColor" opacity="0.21"/>
                <rect x="755" y="195" width="55" height="105" rx="0" fill="none"/>
                <rect x="763" y="185" width="39" height="10" fill="currentColor" opacity="0.21"/>
                <rect x="763" y="185" width="39" height="10" fill="none"/>
                <line x1="755" y1="218" x2="810" y2="218"/>
                <line x1="755" y1="245" x2="810" y2="245"/>
                <line x1="755" y1="272" x2="810" y2="272"/>
                <line x1="782" y1="195" x2="782" y2="300"/>
            </g>

            <!-- Train station building - Streamline Moderne style -->
            <g opacity="0.5">
                <!-- Main horizontal station building -->
                <rect x="865" y="220" width="110" height="80" rx="0" fill="currentColor" opacity="0.22"/>
                <rect x="865" y="220" width="110" height="80" rx="0" fill="none"/>

                <!-- Central tower element -->
                <rect x="900" y="190" width="40" height="30" fill="currentColor" opacity="0.22"/>
                <rect x="900" y="190" width="40" height="30" fill="none"/>
                <rect x="906" y="182" width="28" height="8" rx="4" fill="currentColor" opacity="0.22"/>
                <rect x="906" y="182" width="28" height="8" rx="4" fill="none"/>

                <!-- Streamline horizontal bands -->
                <line x1="865" y1="238" x2="975" y2="238"/>
                <line x1="865" y1="258" x2="975" y2="258"/>
                <line x1="865" y1="278" x2="975" y2="278"/>

                <!-- Vertical divisions -->
                <line x1="890" y1="220" x2="890" y2="300"/>
                <line x1="920" y1="190" x2="920" y2="300"/>
                <line x1="950" y1="220" x2="950" y2="300"/>

                <!-- Curved corner detail (signature Streamline Moderne) -->
                <path d="M 975 228 Q 975 220 967 220" fill="none"/>

                <!-- Clock or decorative circle on tower -->
                <circle cx="920" cy="205" r="7" fill="none"/>
                <circle cx="920" cy="205" r="4" fill="none"/>
                <circle cx="920" cy="205" r="1.5" fill="currentColor" opacity="0.3"/>
            </g>

            <!-- RIGHT SIDE - Tall Buildings (back to front) -->

            <!-- Far back right building -->
            <g opacity="0.5">
                <rect x="1085" y="95" width="50" height="205" rx="0" fill="currentColor" opacity="0.2"/>
                <rect x="1085" y="95" width="50" height="205" rx="0" fill="none"/>
                <rect x="1093" y="78" width="34" height="17" fill="currentColor" opacity="0.2"/>
                <rect x="1093" y="78" width="34" height="17" fill="none"/>
                <line x1="1085" y1="120" x2="1135" y2="120"/>
                <line x1="1085" y1="155" x2="1135" y2="155"/>
                <line x1="1085" y1="190" x2="1135" y2="190"/>
                <line x1="1085" y1="225" x2="1135" y2="225"/>
                <line x1="1085" y1="260" x2="1135" y2="260"/>
                <line x1="1110" y1="95" x2="1110" y2="300"/>
            </g>

            <!-- Middle right building with porthole -->
            <g opacity="0.65">
                <rect x="1025" y="110" width="70" height="190" rx="0" fill="currentColor" opacity="0.3"/>
                <rect x="1025" y="110" width="70" height="190" rx="0" fill="none"/>
                <rect x="1033" y="93" width="54" height="17" fill="currentColor" opacity="0.3"/>
                <rect x="1033" y="93" width="54" height="17" fill="none"/>
                <rect x="1042" y="78" width="36" height="15" rx="7" fill="currentColor" opacity="0.3"/>
                <rect x="1042" y="78" width="36" height="15" rx="7" fill="none"/>
                <line x1="1025" y1="140" x2="1095" y2="140"/>
                <line x1="1025" y1="175" x2="1095" y2="175"/>
                <line x1="1025" y1="210" x2="1095" y2="210"/>
                <line x1="1025" y1="245" x2="1095" y2="245"/>
                <line x1="1025" y1="280" x2="1095" y2="280"/>
                <line x1="1045" y1="110" x2="1045" y2="300"/>
                <line x1="1075" y1="110" x2="1075" y2="300"/>
                <!-- Porthole -->
                <circle cx="1060" cy="200" r="20" fill="currentColor" opacity="0.2"/>
                <circle cx="1060" cy="200" r="20" fill="none"/>
                <circle cx="1060" cy="200" r="12" fill="none"/>
                <circle cx="1060" cy="200" r="5" fill="currentColor" opacity="0.35"/>
            </g>

            <!-- Front right tallest building -->
            <g opacity="0.85">
                <rect x="1125" y="50" width="75" height="250" rx="0" fill="currentColor" opacity="0.4"/>
                <rect x="1125" y="50" width="75" height="250" rx="0" fill="none"/>
                <rect x="1135" y="35" width="55" height="15" fill="currentColor" opacity="0.4"/>
                <rect x="1135" y="35" width="55" height="15" fill="none"/>
                <rect x="1145" y="25" width="35" height="10" rx="5" fill="currentColor" opacity="0.4"/>
                <rect x="1145" y="25" width="35" height="10" rx="5" fill="none"/>
                <circle cx="1162" cy="20" r="4" fill="currentColor"/>
                <line x1="1125" y1="80" x2="1200" y2="80"/>
                <line x1="1125" y1="110" x2="1200" y2="110"/>
                <line x1="1125" y1="140" x2="1200" y2="140"/>
                <line x1="1125" y1="170" x2="1200" y2="170"/>
                <line x1="1125" y1="200" x2="1200" y2="200"/>
                <line x1="1125" y1="230" x2="1200" y2="230"/>
                <line x1="1125" y1="260" x2="1200" y2="260"/>
                <line x1="1125" y1="290" x2="1200" y2="290"/>
                <line x1="1150" y1="50" x2="1150" y2="300"/>
                <line x1="1175" y1="50" x2="1175" y2="300"/>
                <rect x="1192" y="50" width="3" height="250" fill="currentColor" opacity="0.45"/>
            </g>

        </g>
    </svg>

    <!-- Center hero content -->
    <div class="hero-content">
        <h1>Authmoderne</h1>
        <div class="coming-soon-badge">
            Coming Soon
        </div>
        <p class="hero-catchline"><strong>Streamlined authentication for modern Python applications.</strong></p>
        <div class="cta-buttons">
            <a href="https://github.com/frankie567/authmoderne" class="md-button md-button--primary">
                Star on GitHub
            </a>
            <a href="#our-vision" class="md-button">
                Learn More
            </a>
        </div>
    </div>

</div>

<div class="vision-section">

<div class="vision-hero">
<h2>The Future of Python Authentication</h2>
<p class="vision-tagline">Built on years of experience with FastAPI Users and Fief, Authmoderne represents the next generation of authentication—flexible, modern, and truly yours.</p>
</div>

<div class="problem-statement">
<h3>The Problem</h3>
<p>There's no great <strong>framework-agnostic</strong> and <strong>exhaustive</strong> solution for authentication in Python. Developers are forced to choose between limited open-source options or locked-in hosted services like Clerk and Auth0.</p>
</div>

<div class="features-intro">
<h3>What Makes Authmoderne Different</h3>
<p>A complete authentication toolkit designed for developers who value control, flexibility, and modern standards.</p>
</div>

</div>

<div class="grid cards" markdown>

- :lucide-puzzle:{ .lg .middle } **Flexibility & Modularity**

    ***

    Pick exactly what you need. Compose authentication flows from independent, well-designed components that work together seamlessly or standalone.

- :lucide-heart:{ .lg .middle } **Superior Developer Experience**

    ***

    Intuitive APIs, full type hints, comprehensive documentation, and helpful error messages. Built by developers who understand your pain points.

- :lucide-refresh-cw:{ .lg .middle } **Modern Authentication Patterns**

    ***

    Passkeys, social logins, OAuth 2.1 server, and more. Stay ahead of the curve with built-in support for the latest standards.

- :lucide-grid-3x3:{ .lg .middle } **Framework Agnostic**

    ***

    Works with FastAPI, Starlette, and any Python web framework. One authentication toolkit for your entire Python ecosystem.

- :lucide-shield-check:{ .lg .middle } **Security by Design**

    ***

    Industry-standard security practices baked into every layer. You own your authentication, but you don't have to be a security expert.

- :lucide-git-branch:{ .lg .middle } **100% Open Source**

    ***

    Transparent development, no vendor lock-in, community-driven. Authentication is too important to trust to closed systems.

</div>

---

## :lucide-map: Roadmap

<p style="text-align: center; font-size: 1.1em; margin-bottom: 2rem;">We're working hard to bring Authmoderne to life. Here's what we're building:</p>

- [ ] **Core foundations**: API principles, storage providers, basic bricks
- [ ] **Plugin and hooks system**
- [ ] **User management**
    - [ ] Generic identifier: email, username, phone number
    - [ ] Email verification
    - [ ] Multiple emails
- [ ] **Team management**
- [ ] **Authentication methods**
    - [ ] Password
    - [ ] Social login
    - [ ] Passkeys
- [ ] **OAuth 2.1 server**
    - [ ] Machine-to-machine / AI agents authentication

!!! note

    This is a non-ordered list of features we're planning to implement. Priorities will soon be defined based on community feedback. Your input matters!

---

## :lucide-users: Get Involved

<p style="text-align: center; font-size: 1.1em; margin-bottom: 2rem;">Authmoderne is open source and community-driven. We'd love your support!</p>

<div class="grid cards" markdown>

- :lucide-star:{ .lg .middle } **Star the Project**

    ***

    Show your support and stay updated on our progress

    [:lucide-arrow-right: Star on GitHub](https://github.com/frankie567/authmoderne){ .md-button }

- :lucide-eye:{ .lg .middle } **Watch for Updates**

    ***

    Get notified when we release new versions and features

    [:lucide-arrow-right: Watch Repository](https://github.com/frankie567/authmoderne){ .md-button }

- :lucide-messages-square:{ .lg .middle } **Join the Discussion**

    ***

    Share your ideas, requirements, and feedback

    [:lucide-arrow-right: GitHub Discussions](https://github.com/frankie567/authmoderne/discussions){ .md-button }

</div>

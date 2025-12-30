# Software Licenses Reference Guide

## Permissive Licenses

### MIT License

**Full name:** MIT License (Massachusetts Institute of Technology License)
**Category:** Open-source, Permissive
**SPDX Identifier:** MIT

**Key characteristics:**
- Very short and simple
- Allows commercial use, modification, distribution, private use
- Only requires attribution (copyright notice)
- No copyleft - can be used in proprietary software
- No patent grant (implicit at best)

**Best for:**
- Maximum adoption and flexibility
- Libraries intended for wide use
- Projects where simplicity is valued

**Text:** https://opensource.org/licenses/MIT

---

### Apache License 2.0

**Full name:** Apache License, Version 2.0
**Category:** Open-source, Permissive
**SPDX Identifier:** Apache-2.0

**Key characteristics:**
- Permissive with explicit patent grant
- Requires attribution and notice of changes
- Includes patent retaliation clause
- Compatible with GPLv3
- Allows commercial use and proprietary derivatives

**Best for:**
- Corporate projects needing patent protection
- Projects that may be used in enterprise environments
- When explicit patent rights are important

**Text:** https://www.apache.org/licenses/LICENSE-2.0

---

### BSD Licenses

#### BSD 2-Clause (Simplified)
**SPDX Identifier:** BSD-2-Clause

**Key characteristics:**
- Similar to MIT
- Only attribution required
- Very permissive

**Text:** https://opensource.org/licenses/BSD-2-Clause

#### BSD 3-Clause (New/Modified)
**SPDX Identifier:** BSD-3-Clause

**Key characteristics:**
- Adds non-endorsement clause
- Cannot use author's name for promotion without permission

**Text:** https://opensource.org/licenses/BSD-3-Clause

---

### ISC License

**Full name:** ISC License (Internet Systems Consortium)
**Category:** Open-source, Permissive
**SPDX Identifier:** ISC

**Key characteristics:**
- Functionally equivalent to MIT/BSD
- Simplified language
- Used by OpenBSD, npm

**Text:** https://opensource.org/licenses/ISC

---

## Copyleft Licenses

### GNU General Public License (GPL)

#### GPLv2
**SPDX Identifier:** GPL-2.0-only / GPL-2.0-or-later

**Key characteristics:**
- Strong copyleft
- Derivatives must be GPL
- No explicit patent grant
- "Or later" option allows upgrade to GPLv3

**Text:** https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

#### GPLv3
**SPDX Identifier:** GPL-3.0-only / GPL-3.0-or-later

**Key characteristics:**
- Strong copyleft
- Explicit patent grant
- Anti-tivoization clause
- Addresses SaaS loophole partially
- Compatible with Apache 2.0

**Text:** https://www.gnu.org/licenses/gpl-3.0.html

---

### GNU Affero General Public License (AGPL)

**Full name:** GNU Affero General Public License v3.0
**Category:** Open-source, Strong Copyleft
**SPDX Identifier:** AGPL-3.0-only / AGPL-3.0-or-later

**Key characteristics:**
- Strongest copyleft
- Closes the SaaS/network loophole
- Must provide source to users accessing over network
- Used by MongoDB, Grafana

**Best for:**
- SaaS applications
- Preventing proprietary cloud hosting
- Maximum copyleft protection

**Text:** https://www.gnu.org/licenses/agpl-3.0.html

---

### GNU Lesser General Public License (LGPL)

**Full name:** GNU Lesser General Public License
**Category:** Open-source, Weak Copyleft
**SPDX Identifier:** LGPL-2.1-only / LGPL-3.0-only

**Key characteristics:**
- Weak copyleft
- Can be linked with proprietary software
- Modifications to LGPL code must be shared
- Good for libraries

**Best for:**
- Libraries that should be usable in proprietary software
- When you want copyleft for the library itself only

**Text:** https://www.gnu.org/licenses/lgpl-3.0.html

---

### Mozilla Public License 2.0 (MPL)

**Full name:** Mozilla Public License 2.0
**Category:** Open-source, Weak Copyleft
**SPDX Identifier:** MPL-2.0

**Key characteristics:**
- File-level copyleft
- Modified files must be MPL, new files can be proprietary
- Compatible with GPL
- Good balance between permissive and copyleft

**Best for:**
- Projects wanting some copyleft without full GPL restrictions
- When file-level copyleft is sufficient

**Text:** https://www.mozilla.org/en-US/MPL/2.0/

---

### Eclipse Public License 2.0

**Full name:** Eclipse Public License 2.0
**Category:** Open-source, Weak Copyleft
**SPDX Identifier:** EPL-2.0

**Key characteristics:**
- Weak copyleft (module-level)
- Strong patent provisions
- GPL-compatible with secondary license option
- Common in Java ecosystem

**Text:** https://www.eclipse.org/legal/epl-2.0/

---

## Public Domain and Unlicense

### The Unlicense

**Category:** Public Domain Dedication
**SPDX Identifier:** Unlicense

**Key characteristics:**
- Public domain dedication
- Fallback license for jurisdictions without public domain concept
- No restrictions whatsoever

**Text:** https://unlicense.org/

---

### CC0 1.0 Universal

**Full name:** Creative Commons Zero v1.0 Universal
**Category:** Public Domain Dedication
**SPDX Identifier:** CC0-1.0

**Key characteristics:**
- Waives all copyright and related rights
- Fallback public license for jurisdictions that don't recognize waiver
- Recommended by many organizations for data

**Text:** https://creativecommons.org/publicdomain/zero/1.0/

---

### WTFPL

**Full name:** Do What The F*ck You Want To Public License
**Category:** Public Domain-like
**SPDX Identifier:** WTFPL

**Key characteristics:**
- Extremely permissive
- Not recommended for serious projects
- May have legal ambiguities

**Text:** http://www.wtfpl.net/

---

## Specialized Software Licenses

### Server Side Public License (SSPL)

**Full name:** Server Side Public License
**Category:** Source-available (not OSI-approved)

**Key characteristics:**
- Based on AGPL
- Requires sharing entire service stack if offering as a service
- Used by MongoDB
- Not considered open-source by OSI

**Text:** https://www.mongodb.com/licensing/server-side-public-license

---

### Business Source License (BSL/BUSL)

**Full name:** Business Source License
**Category:** Source-available, Time-delayed open-source

**Key characteristics:**
- Source available but not open-source initially
- Converts to open-source after time period (usually 3-4 years)
- Restricts commercial/production use
- Used by MariaDB, HashiCorp, Sentry

**Text:** https://mariadb.com/bsl11/

---

### Elastic License 2.0 (ELv2)

**Category:** Source-available

**Key characteristics:**
- Allows most uses except managed service offering
- Cannot circumvent license key functionality
- Used by Elastic, after SSPL controversy

**Text:** https://www.elastic.co/licensing/elastic-license

---

### Functional Source License (FSL)

**Category:** Source-available, Time-delayed open-source

**Key characteristics:**
- Converts to Apache 2.0 or MIT after 2 years
- More permissive than BSL
- Designed for simplicity

**Text:** https://fsl.software/

---

## License Compatibility Matrix

| From \ To      | MIT | Apache 2.0 | GPLv2 | GPLv3 | LGPL | MPL 2.0 | AGPL |
|----------------|-----|------------|-------|-------|------|---------|------|
| MIT            | Yes | Yes        | Yes   | Yes   | Yes  | Yes     | Yes  |
| Apache 2.0     | No  | Yes        | No    | Yes   | Yes* | Yes     | Yes  |
| BSD            | Yes | Yes        | Yes   | Yes   | Yes  | Yes     | Yes  |
| GPLv2          | No  | No         | Yes   | No*   | No   | No      | No   |
| GPLv3          | No  | No         | No    | Yes   | No   | No      | Yes  |
| LGPL           | No  | No         | No*   | Yes   | Yes  | Yes     | Yes  |
| MPL 2.0        | No  | No         | No    | Yes   | Yes  | Yes     | Yes  |

*With "or later" clause or specific compatibility provisions

---

## Choosing a Software License Decision Tree

1. **Do you want to dedicate to public domain?**
   - Yes → CC0 or Unlicense

2. **Do you care if proprietary software uses your code?**
   - No → MIT, Apache 2.0, or BSD
   - Yes → Continue

3. **Should derivatives always be open-source?**
   - Yes, all derivatives → GPL
   - Yes, but allow linking → LGPL
   - Only modified files → MPL 2.0

4. **Is your software offered as a network service?**
   - Yes, protect against SaaS → AGPL
   - Want to restrict managed services → SSPL (not OSI-approved)

5. **Do you need patent protection?**
   - Yes → Apache 2.0 or GPLv3

6. **Corporate/enterprise adoption priority?**
   - Yes → Apache 2.0 or MIT

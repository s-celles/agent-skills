# Free and Open-Source Software Licenses

## What Makes a License "Free" or "Open Source"?

### The Four Freedoms (FSF)

The Free Software Foundation defines free software as software that respects users' freedom:

0. **Freedom to run** the program for any purpose
1. **Freedom to study** how the program works and modify it
2. **Freedom to redistribute** copies
3. **Freedom to distribute** copies of your modified versions

### The Open Source Definition (OSI)

The Open Source Initiative's definition includes:

1. Free redistribution
2. Source code availability
3. Derived works allowed
4. Integrity of author's source code
5. No discrimination against persons or groups
6. No discrimination against fields of endeavor
7. Distribution of license
8. License must not be specific to a product
9. License must not restrict other software
10. License must be technology-neutral

**Important:** Non-commercial restrictions violate both definitions. A license with NC clause is NOT free/open-source software.

---

## Permissive Licenses

### MIT License

**Full name:** MIT License (Massachusetts Institute of Technology)
**SPDX:** MIT
**Type:** Permissive

**Permissions:**
- Commercial use
- Modification
- Distribution
- Private use

**Requirements:**
- Include copyright notice
- Include license text

**Limitations:**
- No liability
- No warranty

**Best for:**
- Maximum adoption
- Simple, short license
- Don't care if derivatives go proprietary

**Used by:** jQuery, Node.js, React, Ruby on Rails, .NET

**Text:** https://opensource.org/licenses/MIT

---

### Apache License 2.0

**Full name:** Apache License, Version 2.0
**SPDX:** Apache-2.0
**Type:** Permissive with patent grant

**Permissions:**
- Commercial use
- Modification
- Distribution
- Patent use
- Private use

**Requirements:**
- Include copyright notice
- Include license text
- State changes made
- Include NOTICE file (if present)

**Limitations:**
- No liability
- No warranty
- No trademark rights

**Key feature:** Explicit patent grant with termination clause (patent retaliation)

**Best for:**
- Corporate-friendly projects
- When patent protection matters
- Apache ecosystem projects

**Used by:** Android, Apache projects, Kubernetes, TensorFlow

**Text:** https://www.apache.org/licenses/LICENSE-2.0

---

### BSD Licenses

#### BSD 2-Clause (Simplified BSD)
**SPDX:** BSD-2-Clause

Essentially identical to MIT. Two clauses:
1. Retain copyright in source
2. Retain copyright in binary

**Text:** https://opensource.org/licenses/BSD-2-Clause

#### BSD 3-Clause (New BSD)
**SPDX:** BSD-3-Clause

Adds non-endorsement clause: cannot use author's name for promotion without permission.

**Text:** https://opensource.org/licenses/BSD-3-Clause

**Used by:** FreeBSD, NetBSD, Django

---

### ISC License

**Full name:** ISC License (Internet Systems Consortium)
**SPDX:** ISC
**Type:** Permissive

Functionally equivalent to MIT/BSD-2-Clause with simpler language.

**Used by:** OpenBSD, npm default

**Text:** https://opensource.org/licenses/ISC

---

## Copyleft Licenses

### GNU General Public License v3 (GPLv3)

**Full name:** GNU General Public License version 3
**SPDX:** GPL-3.0-only / GPL-3.0-or-later
**Type:** Strong copyleft

**Permissions:**
- Commercial use
- Modification
- Distribution
- Patent use
- Private use

**Requirements:**
- Disclose source code
- Include copyright
- Include license text
- State changes
- Use same license for derivatives

**Limitations:**
- No liability
- No warranty

**Key features:**
- Anti-tivoization (installation information required)
- Explicit patent grant
- Compatible with Apache 2.0

**Best for:**
- Ensuring all derivatives remain free
- Maximum protection of software freedom
- When patent protection matters

**Used by:** GNU tools, WordPress, Drupal, GIMP

**Text:** https://www.gnu.org/licenses/gpl-3.0.html

---

### GNU General Public License v2 (GPLv2)

**Full name:** GNU General Public License version 2
**SPDX:** GPL-2.0-only / GPL-2.0-or-later
**Type:** Strong copyleft

Similar to GPLv3 but:
- No explicit patent grant
- No anti-tivoization
- NOT compatible with Apache 2.0
- Still widely used (Linux kernel is GPLv2-only)

**Note:** "GPLv2 or later" allows upgrade to GPLv3; "GPLv2 only" does not.

**Used by:** Linux kernel (GPLv2-only), Git

**Text:** https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

---

### GNU Affero General Public License (AGPL)

**Full name:** GNU Affero General Public License version 3
**SPDX:** AGPL-3.0-only / AGPL-3.0-or-later
**Type:** Network copyleft (strongest)

Like GPLv3 but adds network clause: if you run modified software as a network service, you must provide source code to users.

**Closes the "SaaS loophole"** where companies could modify GPL software and offer it as a service without sharing changes.

**Best for:**
- Web applications
- SaaS products you want to keep open
- Preventing proprietary cloud offerings

**Used by:** MongoDB (historically), Nextcloud, Mastodon, Grafana

**Text:** https://www.gnu.org/licenses/agpl-3.0.html

---

### GNU Lesser General Public License (LGPL)

**Full name:** GNU Lesser General Public License
**SPDX:** LGPL-2.1-only / LGPL-3.0-only
**Type:** Weak copyleft

**Key characteristic:** Can be linked with proprietary software without the proprietary software becoming LGPL.

**Requirements:**
- Modifications to LGPL code must be LGPL
- Must allow relinking with modified LGPL library
- Proprietary code linking to it remains proprietary

**Best for:**
- Libraries that should be usable in proprietary software
- When you want copyleft for the library itself only

**Used by:** GNU C Library, Qt (dual), GTK

**Text:** https://www.gnu.org/licenses/lgpl-3.0.html

---

### Mozilla Public License 2.0 (MPL)

**Full name:** Mozilla Public License 2.0
**SPDX:** MPL-2.0
**Type:** Weak copyleft (file-level)

**Key characteristic:** File-level copyleft. Modified MPL files must be MPL, but new files can be any license (including proprietary).

**Benefits:**
- Good balance: some protection, high compatibility
- Compatible with GPL
- Simpler compliance than LGPL

**Best for:**
- Projects wanting some copyleft without full GPL requirements
- When file-level copyleft is sufficient

**Used by:** Firefox, Thunderbird, LibreOffice

**Text:** https://www.mozilla.org/en-US/MPL/2.0/

---

### Eclipse Public License 2.0

**Full name:** Eclipse Public License 2.0
**SPDX:** EPL-2.0
**Type:** Weak copyleft (module-level)

Similar to MPL but module-level copyleft. Strong patent provisions. Common in Java ecosystem.

Can include secondary license (GPL) for compatibility.

**Used by:** Eclipse IDE, Jakarta EE

**Text:** https://www.eclipse.org/legal/epl-2.0/

---

## Public Domain Dedications

### CC0 1.0 Universal

**Full name:** Creative Commons Zero v1.0 Universal
**SPDX:** CC0-1.0

Waives all copyright and related rights. Includes fallback license for jurisdictions that don't recognize public domain dedication.

**Best for:**
- Data and databases
- Code snippets
- When you truly want no restrictions

**Note:** Some jurisdictions (France, Germany) don't allow waiving moral rights. CC0 handles this with a fallback.

**Text:** https://creativecommons.org/publicdomain/zero/1.0/

---

### The Unlicense

**SPDX:** Unlicense

Public domain dedication with fallback permissive license.

**Text:** https://unlicense.org/

---

## French Licenses (CeCILL Family)

### CeCILL v2.1

**Full name:** CeCILL Free Software License Agreement v2.1
**Type:** Strong copyleft, GPL-compatible

French equivalent of GPL, explicitly drafted under French law. Officially compatible with GPLv2 and GPLv3.

**Best for:**
- French public sector projects
- Projects requiring explicit French law compatibility
- GPL-equivalent with French legal framework

**Text:** https://cecill.info/licences/Licence_CeCILL_V2.1-en.html

---

### CeCILL-B

**Full name:** CeCILL-B Free Software License Agreement
**Type:** Permissive (BSD-like)

French equivalent of BSD license.

**Text:** https://cecill.info/licences/Licence_CeCILL-B_V1-en.html

---

### CeCILL-C

**Full name:** CeCILL-C Free Software License Agreement
**Type:** Weak copyleft (LGPL-like)

French equivalent of LGPL.

**Text:** https://cecill.info/licences/Licence_CeCILL-C_V1-en.html

---

### Etalab Open License 2.0

**Full name:** Licence Ouverte / Open License 2.0
**Type:** Permissive

French government license for open data. Very permissive, similar to CC BY.

**Text:** https://www.etalab.gouv.fr/licence-ouverte-open-licence/

---

## License Compatibility

### GPL Compatibility Chart

| License | GPLv2 | GPLv3 |
|---------|-------|-------|
| MIT | ✓ | ✓ |
| BSD | ✓ | ✓ |
| ISC | ✓ | ✓ |
| Apache 2.0 | ✗ | ✓ |
| LGPL 2.1 | ✓ | ✓ |
| LGPL 3.0 | ✗ | ✓ |
| MPL 2.0 | ✓* | ✓ |
| CeCILL | ✓ | ✓ |

*MPL 2.0 has explicit GPL compatibility clause

### Combining Licenses

**Permissive + Permissive:** Usually fine, result can be either license
**Permissive + Copyleft:** Result must be copyleft
**Copyleft + Copyleft:** Must be same copyleft family (e.g., GPL + LGPL = GPL)
**Incompatible combinations:** GPLv2-only + Apache 2.0, GPL + proprietary

---

## Quick Selection Guide

| Goal | Recommended License |
|------|---------------------|
| Maximum adoption | MIT or Apache 2.0 |
| Patent protection | Apache 2.0 or GPLv3 |
| Keep derivatives open | GPL |
| Library for any use | MIT, BSD, or LGPL |
| Prevent SaaS abuse | AGPL |
| French law compatibility | CeCILL family |
| Public domain | CC0 or Unlicense |
| File-level copyleft | MPL 2.0 |
| Enterprise-friendly | Apache 2.0 |

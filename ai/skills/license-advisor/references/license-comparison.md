# License Quick Comparison Matrix

## Software Licenses at a Glance

| License | Type | Commercial | Modify | Distribute | Patent Grant | Copyleft | Proprietary Use |
|---------|------|------------|--------|------------|--------------|----------|-----------------|
| MIT | Permissive | Yes | Yes | Yes | No (implicit) | No | Yes |
| Apache 2.0 | Permissive | Yes | Yes | Yes | Yes | No | Yes |
| BSD 2/3 | Permissive | Yes | Yes | Yes | No | No | Yes |
| ISC | Permissive | Yes | Yes | Yes | No | No | Yes |
| GPLv2 | Copyleft | Yes | Yes | Yes | No | Strong | No |
| GPLv3 | Copyleft | Yes | Yes | Yes | Yes | Strong | No |
| AGPL | Copyleft | Yes | Yes | Yes | Yes | Network | No |
| LGPL | Copyleft | Yes | Yes | Yes | Yes | Weak | Linking OK |
| MPL 2.0 | Copyleft | Yes | Yes | Yes | Yes | File-level | New files OK |
| Unlicense | Public Domain | Yes | Yes | Yes | N/A | No | Yes |
| CC0 | Public Domain | Yes | Yes | Yes | N/A | No | Yes |

---

## Creative Commons Licenses at a Glance

| License | Commercial | Derivatives | ShareAlike | Attribution |
|---------|------------|-------------|------------|-------------|
| CC0 | Yes | Yes | No | No |
| CC BY | Yes | Yes | No | Required |
| CC BY-SA | Yes | Yes | Required | Required |
| CC BY-NC | No | Yes | No | Required |
| CC BY-NC-SA | No | Yes | Required | Required |
| CC BY-ND | Yes | No | N/A | Required |
| CC BY-NC-ND | No | No | N/A | Required |

---

## License Categories Summary

### By Freedom Level (Software)

**Most Free → Most Restrictive:**

1. **Public Domain** (CC0, Unlicense)
   - No restrictions whatsoever

2. **Permissive** (MIT, Apache, BSD)
   - Do anything, just give credit

3. **Weak Copyleft** (LGPL, MPL)
   - Modifications shared, but can combine with proprietary

4. **Strong Copyleft** (GPL)
   - Derivatives must be same license

5. **Network Copyleft** (AGPL)
   - Even network use triggers sharing requirement

6. **Source-Available** (SSPL, BSL)
   - Viewable but restricted use

7. **Proprietary**
   - All rights reserved

---

### By Use Case

| Use Case | Recommended Licenses |
|----------|---------------------|
| Maximum adoption | MIT, Apache 2.0 |
| Library for any project | MIT, BSD, Apache 2.0 |
| Ensure derivatives stay open | GPL |
| Library with some protection | LGPL, MPL 2.0 |
| SaaS/cloud application | AGPL |
| Enterprise-friendly | Apache 2.0 |
| Data/databases | CC0, ODbL |
| Educational content | CC BY, CC BY-SA |
| Artistic work for sharing | CC BY |
| Artistic work with control | CC BY-NC-ND |
| Font | OFL |
| Hardware design | CERN-OHL |
| AI model | OpenRAIL |

---

## Key Characteristics Comparison

### Patent Protection

| License | Patent Grant | Patent Retaliation |
|---------|--------------|-------------------|
| MIT | None (implicit) | No |
| BSD | None | No |
| Apache 2.0 | Explicit | Yes |
| GPLv2 | None | No |
| GPLv3 | Explicit | Yes |
| MPL 2.0 | Explicit | Yes |
| LGPL v3 | Explicit | Yes |

---

### Attribution Requirements

| License | How to Attribute |
|---------|-----------------|
| MIT | Include copyright notice and license text |
| Apache 2.0 | NOTICE file, copyright, license, state changes |
| BSD | Copyright notice in source and binary |
| GPL | Copyright, license, source offer |
| CC BY | Creator name, title, license, link, indicate changes |

---

### Compatibility Quick Reference

**Can be combined with GPL:**
- MIT ✓
- BSD ✓
- Apache 2.0 ✓ (GPLv3 only)
- ISC ✓
- MPL 2.0 ✓
- LGPL ✓

**Cannot be combined with GPL:**
- Apache 2.0 + GPLv2
- CDDL
- EPL 1.0 (EPL 2.0 with secondary license OK)

---

## Dual Licensing Patterns

### Open Core
- Core: Open source (GPL, MIT, etc.)
- Extensions: Proprietary

### Community/Commercial
- Open source license for open source use
- Commercial license for proprietary use

**Examples:**
| Project | Open License | Commercial |
|---------|--------------|------------|
| MySQL | GPL | Proprietary |
| Qt | LGPL/GPL | Commercial |
| GitLab | MIT (CE) | Proprietary (EE) |
| MongoDB | SSPL | Commercial |

---

## License Selection Cheat Sheet

### For Software

**Want maximum adoption?**
→ MIT or Apache 2.0

**Want to protect against patent trolls?**
→ Apache 2.0 or GPLv3

**Want derivatives to remain open?**
→ GPL (GPLv3 recommended)

**Building a library?**
→ MIT (permissive) or LGPL (some protection)

**Building a SaaS product?**
→ AGPL (if you want copyleft) or MIT (if not)

**Corporate environment?**
→ Apache 2.0

**Don't care at all?**
→ CC0 or Unlicense

---

### For Creative Works

**Want credit?**
→ CC BY

**Want credit + keep derivatives open?**
→ CC BY-SA

**Want credit + no commercial use?**
→ CC BY-NC

**Want credit + no modifications?**
→ CC BY-ND

**Maximum restriction while sharing?**
→ CC BY-NC-ND

**No restrictions?**
→ CC0

---

## Common Pitfalls

### License Traps to Avoid

1. **GPL + Proprietary Mixing**
   - GPL code cannot be combined with proprietary code in a single work

2. **NC Ambiguity**
   - "Non-commercial" is not well-defined; internal corporate use may or may not qualify

3. **Apache 2.0 + GPLv2**
   - These are incompatible; use GPLv3 or MIT instead

4. **SSPL Confusion**
   - Not OSI-approved; projects may reject as "not open source"

5. **Jurisdiction Assumptions**
   - Some concepts (public domain, fair use) vary by country

6. **Moral Rights**
   - Cannot be waived in many jurisdictions (France, Germany, etc.)

7. **Patent Implicit vs Explicit**
   - MIT has no explicit patent grant; may be risky for patent-heavy software

8. **SaaS Loophole**
   - GPL doesn't require source sharing for network services; use AGPL if this matters

---

## Quick Decision Matrix

| Question | Yes | No |
|----------|-----|-----|
| Allow commercial use? | MIT, Apache, GPL, CC BY | CC BY-NC, proprietary |
| Allow modifications? | MIT, GPL, CC BY, CC BY-SA | CC BY-ND, CC BY-NC-ND |
| Require attribution? | Apache, GPL, CC BY | CC0, Unlicense |
| Keep derivatives open? | GPL, CC BY-SA | MIT, BSD, CC BY |
| Need patent protection? | Apache 2.0, GPLv3 | MIT, BSD |
| Enterprise adoption? | Apache 2.0, MIT | AGPL, GPL |
| Protect against SaaS? | AGPL, SSPL | GPL, MIT |

---

## License Text Links

### Software
- MIT: https://opensource.org/licenses/MIT
- Apache 2.0: https://www.apache.org/licenses/LICENSE-2.0
- GPLv3: https://www.gnu.org/licenses/gpl-3.0.html
- LGPL: https://www.gnu.org/licenses/lgpl-3.0.html
- MPL 2.0: https://www.mozilla.org/en-US/MPL/2.0/
- AGPL: https://www.gnu.org/licenses/agpl-3.0.html

### Creative Works
- CC Licenses: https://creativecommons.org/licenses/
- CC0: https://creativecommons.org/publicdomain/zero/1.0/
- OFL: https://scripts.sil.org/OFL

### Data
- ODC Licenses: https://opendatacommons.org/licenses/

### Hardware
- CERN OHL: https://ohwr.org/cernohl

### Helpful Tools
- Choose a License: https://choosealicense.com/
- SPDX License List: https://spdx.org/licenses/
- TLDRLegal: https://tldrlegal.com/
- Creative Commons Chooser: https://creativecommons.org/choose/

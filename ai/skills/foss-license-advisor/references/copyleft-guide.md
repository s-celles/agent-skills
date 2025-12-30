# Understanding Copyleft: A Deep Dive

## What is Copyleft?

Copyleft is a licensing strategy that uses copyright law to ensure that derivative works remain free. Instead of placing work in the public domain (where anyone can make it proprietary), copyleft licenses require that modifications and distributions preserve the same freedoms.

**The key principle:** "If you use my free code, your code must also be free."

---

## The Philosophy Behind Copyleft

### Free Software Foundation (FSF) Perspective

The FSF created copyleft (starting with GPL) to protect software freedom. Their view:

- **Permissive licenses** allow proprietary forks, which can "take" from the commons without giving back
- **Copyleft** ensures the software freedom is preserved in all derivatives
- The goal is to maximize user freedom, not developer convenience

### Pragmatic Perspective

Some developers choose copyleft for practical reasons:

- Prevents competitors from taking code proprietary
- Encourages contributions back to the project
- Creates a "level playing field" - everyone plays by the same rules
- Enables dual licensing business models

---

## Types of Copyleft

### Strong Copyleft

**Definition:** Any work that uses or incorporates the copyleft code must be released under the same copyleft license.

**Examples:** GPL, AGPL, CeCILL

**Scope:** Entire derivative work

```
┌─────────────────────────────────────┐
│         Your Application            │
│  ┌─────────────┐ ┌───────────────┐ │
│  │  GPL Code   │ │  Your Code    │ │
│  │             │ │               │ │
│  └─────────────┘ └───────────────┘ │
│         ALL MUST BE GPL             │
└─────────────────────────────────────┘
```

**When copyleft applies:**
- Static linking
- Dynamic linking (for GPL)
- Including code in your source
- Modifying the original code

---

### Weak Copyleft

**Definition:** Only modifications to the original code must be shared under the same license. New code can be any license.

**Examples:** LGPL, MPL, CeCILL-C

**Scope:** The library/module itself, not the whole work

```
┌─────────────────────────────────────┐
│         Your Application            │
│  ┌─────────────┐ ┌───────────────┐ │
│  │  LGPL Lib   │ │  Your Code    │ │
│  │  (stays     │ │  (can be      │ │
│  │   LGPL)     │ │   proprietary)│ │
│  └─────────────┘ └───────────────┘ │
│     Library LGPL, rest is yours     │
└─────────────────────────────────────┘
```

#### LGPL (Library-level)

- Modifications to LGPL code → LGPL
- Code that links to LGPL library → any license
- Must allow relinking with modified library

#### MPL (File-level)

- Modified MPL files → MPL
- New files → any license
- Simpler compliance than LGPL

---

### Network Copyleft (AGPL)

**Definition:** Like strong copyleft, but also triggers when software is accessed over a network (not just distributed).

**The SaaS Loophole:** GPL only requires sharing source when you *distribute* the software. Running modified software as a web service isn't "distribution," so you never have to share changes.

**AGPL closes this:** If users interact with your modified AGPL software over a network, you must offer them the source code.

```
┌─────────────────────────────────────┐
│         Cloud Service               │
│  ┌─────────────────────────────┐   │
│  │     Modified AGPL Code      │   │
│  │                             │   │
│  └──────────────┬──────────────┘   │
│                 │                   │
│            Network Users            │
│            Must be able to          │
│            get source code          │
└─────────────────────────────────────┘
```

---

## Copyleft Scope: What Triggers It?

### GPL Interpretation

The GPL uses the concept of "derivative work" from copyright law, but adds its own interpretation:

| Action | Triggers GPL? |
|--------|--------------|
| Copy-paste GPL code into your project | Yes |
| Modify GPL code | Yes |
| Static link to GPL library | Yes |
| Dynamic link to GPL library | Yes* |
| Use GPL command-line tool | No |
| Pipe data to GPL program | No |
| Read GPL program's output | No |
| Run GPL program as subprocess | Debated |

*FSF says yes; some disagree. This is the "linking exception" debate.

### The System Library Exception

GPL includes an exception for "System Libraries" - you don't have to provide GPL'd versions of standard OS libraries (libc, etc.) even if they're linked.

### Linux Kernel Syscall Exception

The Linux kernel explicitly states that userspace programs using syscalls are NOT derivative works. This allows proprietary software to run on Linux.

---

## Copyleft in Practice

### Compliance Requirements

#### For GPL/AGPL:

1. **Include license text** with distribution
2. **Include copyright notices**
3. **Provide source code** (or written offer)
4. **State modifications** made
5. **No additional restrictions** beyond GPL

#### For LGPL:

All of the above, plus:
- Must allow relinking with modified library
- For static linking, must provide object files

#### For MPL:

- Modified MPL files must stay MPL
- Include MPL license
- Document changes

### Common Compliance Failures

1. **Not providing source:** Distributing binary without source offer
2. **Incomplete source:** Missing build scripts, dependencies
3. **Adding restrictions:** DRM, additional terms
4. **Stripping notices:** Removing copyright headers
5. **Tivoization:** Hardware that refuses modified software (GPLv3 addresses this)

---

## Choosing Your Copyleft Strength

### Choose Strong Copyleft (GPL) when:

- You believe all software should be free
- You want to prevent proprietary forks
- You're building an ecosystem (like Linux)
- You want dual licensing revenue model
- You don't care about adoption in proprietary software

### Choose Network Copyleft (AGPL) when:

- Your software will be used as a service
- You want to prevent proprietary SaaS offerings
- You're building web applications
- Cloud providers using your code should contribute back

### Choose Weak Copyleft (LGPL/MPL) when:

- You want copyleft benefits for your code
- But want to allow proprietary use/linking
- You're building a library
- Adoption in proprietary software matters
- You want simpler compliance than GPL

### Choose Permissive (MIT/Apache) when:

- Maximum adoption is the priority
- You don't care about proprietary forks
- Your employer requires permissive
- You're building standards/reference implementations

---

## Copyleft Compatibility

### The Compatibility Problem

Different copyleft licenses can be incompatible because each requires derivatives to use its specific license.

```
GPLv2 code + GPLv3 code = ?
Both require their license for derivatives.
If GPLv2-only: Incompatible!
If GPLv2-or-later: OK, use GPLv3.
```

### GPL Version Compatibility

| License A | License B | Compatible? |
|-----------|-----------|-------------|
| GPLv2-only | GPLv3-only | No |
| GPLv2+ | GPLv3+ | Yes (use GPLv3+) |
| GPLv2+ | GPLv3-only | Yes (use GPLv3) |
| LGPL 2.1 | GPL 3.0 | Yes (becomes GPL) |
| AGPL 3.0 | GPL 3.0 | Yes (becomes AGPL) |

### Cross-Family Compatibility

| License | GPL Compatible? |
|---------|-----------------|
| MIT | Yes |
| BSD | Yes |
| Apache 2.0 | GPLv3 only |
| MPL 2.0 | Yes (with clause) |
| LGPL | Yes (becomes GPL) |
| CDDL | No |
| EPL 1.0 | No |

---

## Dual Licensing with Copyleft

### The Business Model

Many companies use copyleft strategically:

1. Release software under GPL
2. Offer commercial license for proprietary use
3. Competitors must either:
   - Open source their code
   - Pay for commercial license

**Examples:**
- MySQL (GPL + Commercial)
- Qt (LGPL/GPL + Commercial)
- MongoDB (originally AGPL)

### Requirements for Dual Licensing

- You must own all the code (or have contributor agreements)
- Third-party copyleft code can't be relicensed
- Contributors must assign rights or sign CLA

---

## Common Copyleft Myths

### Myth: "GPL means I can't sell software"

**Reality:** GPL explicitly allows commercial use and sale. You just must provide source code.

### Myth: "If I use GPL code, all my code becomes GPL"

**Reality:** Only if you create a derivative work. Using GPL tools, reading output, or calling as subprocess typically doesn't trigger copyleft.

### Myth: "LGPL is just GPL for libraries"

**Reality:** Any code can be LGPL. The difference is linking scope, not code type.

### Myth: "Copyleft is viral and infects everything"

**Reality:** Copyleft has clear scope rules. It doesn't "spread" beyond derivative works. The "viral" metaphor is misleading and often used to create fear.

### Myth: "I can't use GPL code in my company"

**Reality:** You can use GPL code internally without sharing. Copyleft only triggers on *distribution*.

---

## Copyleft and Patents

### GPLv3 Patent Provisions

GPLv3 includes explicit patent grant and protection:

1. **Patent grant:** Contributors grant patent rights for their contributions
2. **Patent retaliation:** If you sue for patent infringement, your license terminates
3. **Anti-tivoization:** Must provide installation information

### Why This Matters

- Protects users from patent trolls
- Prevents "patent ambush" (contribute code, then sue users)
- Addresses concerns that GPLv2 didn't explicitly handle

---

## Summary: Copyleft Spectrum

```
More Permissive ←────────────────────────→ More Copyleft

Public    MIT/BSD    Apache    MPL    LGPL    GPL    AGPL
Domain                         2.0

          ↑          ↑         ↑      ↑       ↑      ↑
     No copyleft   Patent   File   Library  Full  Network
                   grant    level   level  copyleft copyleft
```

Choose based on your values, business model, and community expectations.

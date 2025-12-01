---
marp: true
title: Product Documentation Guide
author: 24f1000043@ds.study.iitm.ac.in
theme: gaia
paginate: true
---

<!-- _class: lead -->
<!-- _footer: 24f1000043@ds.study.iitm.ac.in -->

<style>
section {
  font-family: 'Arial', sans-serif;
  line-height: 1.35;
}
code {
  background: #eee;
  padding: 0.15rem 0.3rem;
  border-radius: 4px;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, "Roboto Mono", monospace;
}
</style>

# Product Documentation Guide
## Q4 Technical Overview

**Contact:** 24f1000043@ds.study.iitm.ac.in

---

<!-- _backgroundColor: #f7f9fb -->
# Algorithmic Efficiency

Our new search indexing uses an optimized sort, reducing latency significantly.

The time complexity is defined as:

$$
T(n) = O(n \log n) + \sum_{i=1}^{n} \frac{1}{i}
$$

Notes:
- The harmonic term grows like $O(\log n)$, so overall complexity is $O(n\log n)$ asymptotically.

---

<!-- _class: lead -->
<!-- _color: #003366 -->
# Custom Styled Slide

This slide demonstrates **Marp Directives** in action:
- Custom background color via directive
- Custom text color directive
- Page numbers come from `paginate: true`

---

<!-- Option A: Remote background using Marp inline bg syntax (very explicit) -->
![bg cover](https://images.unsplash.com/photo-1461749280684-dccba630e2f6?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80)

# Infrastructure

This slide includes a background image (cover).

1. **Version Control**: Git-based flow  
2. **CI/CD**: Automated builds  
3. **Format**: Markdown → PDF / HTML / PPTX

---

<!-- Option B: Local image (use this if your validator requires local files).
     Put an image at 'images/bg.jpg' in the repo and uncomment the directive below.
-->
<!-- _backgroundImage: images/bg.jpg -->
<!-- _backgroundFit: cover -->
<!-- _footer: "Docs v1.0 — 24f1000043@ds.study.iitm.ac.in" -->

# Contact Information

For more details on this documentation standard:

**Email:** 24f1000043@ds.study.iitm.ac.in

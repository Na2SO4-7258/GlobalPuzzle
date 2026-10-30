# Reference additions checked on 2026-10-31

The bibliography was expanded from 21 to 35 distinct works. All 14 additions are cited in `main.tex`; none are included through `\nocite`. The additional related-work methods are not presented as experimentally evaluated baselines.

| BibTeX key | Publication | Supported use in the manuscript | Primary verification source |
| --- | --- | --- | --- |
| `doersch2015context` | Doersch, Gupta, and Efros, ICCV 2015, pp. 1422–1430 | Learning representations by predicting relative patch positions | [Official proceedings](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Doersch_Unsupervised_Visual_Representation_ICCV_2015_paper.html) |
| `noroozi2016jigsaw` | Noroozi and Favaro, ECCV 2016, pp. 69–84 | Jigsaw arrangement as a representation-learning task | [Springer chapter](https://link.springer.com/chapter/10.1007/978-3-319-46466-4_5) |
| `santacruz2017deeppermnet` | Santa Cruz, Fernando, Cherian, and Gould, CVPR 2017, pp. 3949–3957 | Differentiable permutation prediction with Sinkhorn normalization | [Official proceedings PDF](https://openaccess.thecvf.com/content_cvpr_2017/papers/Santa_Cruz_DeepPermNet_Visual_Permutation_CVPR_2017_paper.pdf) |
| `yang2011particle` | Yang, Adluru, and Latecki, CVPR 2011, pp. 2873–2880 | Particle filtering for image jigsaw assembly | [Author manuscript record](https://pubmed.ncbi.nlm.nih.gov/27795660/), [publisher DOI metadata](https://api.crossref.org/works/10.1109/CVPR.2011.5995535) |
| `andalo2012quadratic` | Andaló, Taubin, and Goldenstein, SIBGRAPI 2012, pp. 63–70 | Quadratic programming for image puzzle assembly | [Author publication page](https://fernanda.andalo.net.br/publications/andalo12sibgrapi/), [author CV](https://www.fernanda.andalo.net.br/files/cv.pdf) |
| `son2014loops` | Son, Hays, and Cooper, ECCV 2014, pp. 32–46 | Consistent loops as structural constraints | [Springer chapter](https://link.springer.com/chapter/10.1007/978-3-319-10599-4_3) |
| `son2016consensus` | Son, Moreno, Hays, and Cooper, CVPR 2016, pp. 1193–1201 | Small-piece difficulty and growing geometric consensus | [Official proceedings](https://www.cv-foundation.org/openaccess/content_cvpr_2016/html/Son_Solving_Small-Piece_Jigsaw_CVPR_2016_paper.html) |
| `huroyan2020laplacian` | Huroyan, Lerman, and Wu, SIAM Journal on Imaging Sciences 13(4), 2020, pp. 1717–1753 | Graph connection Laplacian for recovering fragment rotations | [Author manuscript and journal reference](https://arxiv.org/abs/1811.03188) |
| `sholomon2014generalized` | Sholomon, David, and Netanyahu, AAAI 2014, pp. 2839–2845 | Genetic assembly with unknown orientations and piece faces | [Official proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/9148) |
| `sholomon2014multiple` | Sholomon, David, and Netanyahu, GECCO 2014, pp. 1191–1198 | Mixed puzzles with unknown dimensions and orientations | [Author manuscript and original publication reference](https://arxiv.org/abs/1711.06766) |
| `sholomon2016dnnbuddies` | Sholomon, David, and Netanyahu, ICANN 2016, pp. 170–178 | Learned pairwise adjacency estimation | [Springer chapter](https://link.springer.com/chapter/10.1007/978-3-319-44781-0_21) |
| `paumard2018local` | Paumard, Picard, and Tabia, ICIP 2018, pp. 1018–1022 | Relative positions from local feature co-occurrences | [Author manuscript](https://arxiv.org/abs/1807.03155), [publisher DOI metadata](https://api.crossref.org/works/10.1109/ICIP.2018.8451094) |
| `sizikova2018wall` | Sizikova and Funkhouser, ACM JOCCH 11(1), article 3, 2018, pp. 1–17 | Archaeological wall-painting reconstruction as a related application | [Author publication list](https://esizikova.github.io/), [publisher DOI metadata](https://api.crossref.org/works/10.1145/3084547) |
| `micikevicius2018mixed` | Micikevicius et al., ICLR 2018 | The mixed-precision training technique already stated in Experimental Setup | [Author manuscript](https://arxiv.org/abs/1710.03740); its PDF explicitly identifies ICLR 2018 publication |

## Metadata and scope checks

- Son 2016 is titled **Solving Small-Piece Jigsaw Puzzles by Growing Consensus** in the official proceedings. Its supplementary PDF uses “Maximizing Consensus”; the bibliography follows the proceedings title.
- The author surname **Santa Cruz** is preserved as a compound surname. DeepPermNet's page range is taken from the printed proceedings PDF, not a search snippet.
- Andaló's coauthor is **Siome Goldenstein**, as confirmed by the author's publication page and CV; the Crossref record has a spelling discrepancy.
- Sholomon's GECCO and DNN-Buddies papers are dated **2014** and **2016**, respectively, rather than their later arXiv upload years.
- Huroyan's article uses the **2020 journal publication**, rather than its 2018 preprint date.
- The wall-painting article uses the **2018 journal issue year**, consistent with the author's publication list. Crossref records the earlier online publication on 7 December 2017. Its 2016 workshop version is not added as a separate reference.
- Context prediction and jigsaw pretraining are described as representation-learning work, not as GAP benchmark solvers. Geometric consistency methods are distinguished from simple pairwise-score aggregation.
- Existing GAP/PuzzleFlow, PuzLM, and JPDVT records were also checked against [the GAP author record](https://arxiv.org/abs/2605.12077), [the PuzLM publisher volume](https://link.springer.com/book/10.1007/978-3-032-37281-9), and [the JPDVT official proceedings](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Solving_Masked_Jigsaw_Puzzles_with_Diffusion_Vision_Transformers_CVPR_2024_paper.html). Their existing publication details were retained.

Source URLs are also recorded beside the new entries in `references.bib`. This check validates reference identity, bibliographic details, and the cited method descriptions; it does not independently reproduce the paper's experimental results.

# 기존 연구

단일 세포 분석은 틈새 연구 분야에서 시작하여 이제는 잘 정립된 연구 분야로 발전했습니다.
결과적으로, 우리는 이 주제에 대한 책을 만들거나 가이드와 튜토리얼을 제공하는 첫 번째 주자가 아닙니다.
이어지는 섹션에서는 단일 세포 분석 교육을 목표로 하는 두 가지 주목할 만하고 진행 중인 이니셔티브를 검토하고, 이 책과의 유사점과 차이점을 모두 강조합니다.

(introduction-prior-art-key-takeaway-1)=

## Bioconductor OSCA 및 OSTA 서적

Bioconductor를 사용한 단일 세포 분석 오케스트레이션(Bioconductor OSCA) {cite}`osca`는 https://bioconductor.org/books/release/OSCA/ 에서 온라인으로 제공되며, R 기반 Bioconductor 생태계 {cite}`pa:Huber2015`를 사용하여 단일 세포 {term}`RNA`-{term}`서열 분석`(scRNA-seq) 데이터를 분석하기 위한 일반적인 워크플로우를 가르치도록 설계된 온라인 서적입니다.
같은 제목의 함께 제공되는 논문 {cite}`Amezquita2020`은 Bioconductor를 사용한 단일 세포 분석에 대한 개요를 제공하며, 온라인 서적은 자세한 설명과 광범위한 코드 예제를 통해 더 심층적인 내용을 다룹니다.

OSCA 서적은 기본적인 scRNA-seq 분석에 대해 매우 포괄적으로 다루며, 명확한 설명과 상세한 워크플로우 예제를 제공합니다.
그러나 단일 세포 ATAC-seq(scATAC-seq)와 같은 다른 단일 세포 오믹스까지 다루지는 않습니다.
공간 전사체학은 보완 서적인 Bioconductor를 사용한 공간 분해 전사체학 분석 오케스트레이션(Bioconductor OSTA)에서 별도로 다루며, https://lmweber.org/OSTA-book/ 에서 확인할 수 있습니다.

두 서적 모두 Bioconductor 생태계에 맞춰져 있으므로 Bioconductor 내에서 사용 가능한 도구만 독점적으로 사용합니다.
이러한 도구는 매우 효과적이지만, 서적 자체에서도 인정하듯이 모든 분석에 항상 최적의 솔루션을 제공하지는 않을 수 있습니다.
전반적으로 Bioconductor 서적은 R에 대한 기초 지식과 생물학에 대한 탄탄한 배경 지식을 갖춘 개인이 Bioconductor 프레임워크 내에서 단일 세포 및 공간 전사체학 데이터를 분석하는 방법을 배우기에 특히 적합합니다.

(introduction-prior-art-key-takeaway-2)=

## 단일 세포 RNA-seq 분석의 현재 모범 사례: 튜토리얼

Malte Lücken과 Fabian Theis의 단일 세포 {term}`RNA`-Seq 분석의 현재 모범 사례: 튜토리얼 {cite}`pa:Lücken2019`은 scRNA-seq 분석을 위한 모범 사례를 소개합니다.
이 논문의 핵심 기여는 잠재적인 분석 단계를 검토할 뿐만 아니라 독립적인 벤치마크를 기반으로 모범 사례를 추천하는 데 있습니다.
특정 모범 사례 가이드라인이 없는 경우 저자는 분석 접근 방식에 대한 일반적인 권장 사항을 제공합니다.
독립적인 벤치마크에 집중한다는 기본 아이디어는 우리 연구에 상당한 영감을 주었습니다.
이 논문은 Haber et al. {cite}`pa:Haber2017`의 [쥐 소장 상피 영역의 예제 분석](https://github.com/theislab/single-cell-tutorial/)으로 보완됩니다.

Bioconductor OSCA와 비교하여, 이 논문과 관련 분석은 특정 도구 생태계에 제약을 받지 않으므로 다루는 주제의 범위에 대해 더 넓은 관점을 제공합니다.
그러나 함께 제공되는 예제 분석은 초보자에게 친숙하지 않고 오래되었습니다.
Bioconductor OSCA와 유사하게, Lücken & Theis는 RNA 속도, 공간 전사체학 또는 다중 오믹스와 같은 최신 개발 사항을 다루지 않습니다.

이러한 한계에도 불구하고, 우리는 이 논문을 이 분야에 대한 귀중한 소개 자료이자 scRNA-seq 분석의 초기 모범 사례에 대한 가이드로서 강력히 추천합니다.
이 책의 장들은 최신 모범 사례를 기반으로 하며, 이 분야에 대한 업데이트된 관점을 제공합니다. 또한, 이 책의 워크플로우는 더 자세히 설명되어 독자가 방법을 효과적으로 적용하는 데 필요한 배경 정보를 제공합니다.
우리는 논문과 함께 제공되는 예제 사례 연구에 의존하지 말고, 보다 포괄적이고 최신 정보를 얻으려면 이 책의 상세한 장을 탐색할 것을 권장합니다.

## 참고 문헌

```{bibliography}
:filter: docname in docnames
:labelprefix: pa
```
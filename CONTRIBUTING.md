# 기여하기

## 우리의 철학

우리는 이 책이 사람들에게 단일 세포 및 공간 데이터 분석을 소개하는 자료가 되는 것을 목표로 하며, 초심자와 숙련된 분석가 모두가 올바르게 작업을 수행할 수 있도록 보장합니다. 우리의 권장 사항이 모범 사례를 반영하도록 하기 위해, 우리는 전적으로 외부의 독립적인 벤치마크에 의존하려고 노력합니다.

## 어떻게 기여할 수 있나요?

우리는 기여를 따뜻하게 환영하며, 특히 우리의 모범 사례를 최신 상태로 유지하는 데 도움이 되는 기여를 환영합니다! 그러나 [위](#우리의-철학)에서 언급했듯이 이러한 권장 사항은 높은 기준을 따릅니다.

새로운 튜토리얼, 수정 또는 확장을 제안하는 경우, 먼저 이슈를 열어 우리와 아이디어를 논의하는 것을 강력히 권장합니다. 우리는 항상 최신 개발에 대해 배우고 싶어하며 현재의 모범 사례에 대해 기꺼이 논의합니다. 또한 [퀴즈 및 플래시카드](#사용자-정의-퀴즈-및-플래시카드-만들기) 형태의 기여도 권장합니다. 어떤 제안이든: 이슈를 열고 연락주세요!

[![이슈 열기](https://img.shields.io/badge/Open%20Issue-blue?logo=github)](https://github.com/theislab/single-cell-best-practices/issues/new?title=Your+Issue+Title&body=Describe+your+issue+here)

## 책의 구조

`jupyter_book` 폴더에는 책의 소스 콘텐츠와 구성이 포함되어 있습니다. 여러 구성 파일 외에도 모든 챕터는 `conditions` 폴더와 같이 각 섹션 폴더로 그룹화됩니다. 각 섹션에는 관련 노트북과 [관련 파일](#모든-챕터의-필수-파일)이 포함되어 있습니다.

폴더 레이아웃의 예는 다음과 같습니다:

```bash
├── conditions
│   ├── compositional_keytakeaways.txt
│   ├── compositional.bib
│   ├── compositional.ipynb
│   ├── compositional.yml
│   ├── differential_gene_expression_keytakeaways.txt
│   ├── differential_gene_expression.bib
│   ├── differential_gene_expression.ipynb
│   ├── differential_gene_expression.yml
│   ├── gsea_pathway_keytakeaways.txt
│   └── ...
├── ...
├── _toc.yml
├── _config.yml
├── acknowledgements.md
├── CHANGELOG.md
├── glossary.md
├── outlook.md
├── preamble.md
├── _static
│   ├── book.css
│   ├── book.js
│   ├── favicon.ico
│   ├── images
│   │   ├── conditions
│   │   │   ├── compositional.jpg
│   │   │   └── differential_gene_expression.jpg
│   │   └── ...
```

## 책 빌드하기

책을 빌드하려면 다음 종속성을 설치해야 합니다:

1. jupyter-book
2. jupytext
3. beautifulsoup4

[여기에서 예제 Conda 환경을 찾을 수 있습니다](https://github.com/theislab/single-cell-best-practices/blob/development/environment.yml).

환경 파일을 사용하여 다음 명령을 실행하여 책을 빌드할 환경을 만듭니다.

```bash
conda env create -f environment.yml
```

그런 다음 책을 빌드하는 것은 간단합니다:

```bash
make
```

그러면 전체 책이 빌드됩니다. 이것은 노트북을 실행하지 않으며 업데이트된 챕터는 별도의 단계에서 업데이트해야 합니다.

빌드 디렉토리를 정리하려면 다음을 실행하십시오:

```bash
make clean
```

### 개별 챕터 빌드하기

모든 챕터는 Jupyter 노트북으로 제공되며 종단 간 실행 가능합니다. 챕터에 대한 도구의 다양한 요구 사항으로 인해 모든 챕터를 빌드할 수 있는 단일 환경을 제공할 수 없습니다. 따라서 챕터별로 최소한의 Conda 환경을 제공하기로 결정했습니다. 이는 각 폴더에서 찾을 수 있습니다.

> [!NOTE]
> 선택한 환경 파일로 다음 명령을 실행하여 빌드하려는 챕터의 환경을 만듭니다.
>
> ```bash
> conda env create -f CHAPTER-NAME.yml
> ```
>
> 이제 노트북의 모든 셀을 실행할 수 있습니다.

## 기여자를 위한 스타일 가이드

### 모든 챕터의 필수 파일

각 챕터에는 몇 가지 필수 파일이 함께 제공됩니다. `.ipynb` 노트북에는 주요 내용이 포함되어 있으며 함께 제공되는 `.bib` 파일에서 인용을 가져옵니다. `.yml` 파일은 [위](#개별-챕터-빌드하기)에서 설명한 대로 최소한의 Conda 환경을 정의합니다. 마지막으로, `_keytakeaways.txt` 파일은 지정된 [형식](#핵심-내용-환경-및-lamin-드롭다운)에 따라 챕터의 주요 아이디어를 요약합니다.

```bash
├── SECTION-NAME
│   ├── CHAPTER-NAME.ipynb
│   ├── CHAPTER-NAME.bib
│   ├── CHAPTER-NAME.yml
│   ├── CHAPTER-NAME_keytakeaways.txt
│   ├── ...
```

### 노트북 구조

각 `.ipynb` 노트북은 다음 표준 구조를 따라야 합니다:

1. 🧠 **제목**
2. 🔽 **드롭다운 섹션**
   - 핵심 내용
   - 환경 설정
   - Lamin 설정
3. 📖 **주요 내용**
4. 🔗 **참고 항목** _(드롭다운)_
5. ❓ **퀴즈 / 플래시카드**
6. 📚 **참고 문헌**
7. 👥 **기여자**

제목 바로 뒤에 오는 모든 드롭다운은 해당 [요구 사항](#핵심-내용-환경-및-lamin-드롭다운)을 충족하면 자동으로 삽입됩니다. 또한 각 챕터는 다루는 주요 개념을 강화하는 몇 가지 질문으로 마무리되어야 합니다. [아래](#사용자-정의-퀴즈-및-플래시카드-만들기)에서 사용자 정의 형식으로 퀴즈와 플래시카드를 만드는 방법에 대한 지침을 찾을 수 있습니다. 또한 책의 챕터를 빠르고 효과적으로 만들 수 있는 챕터 [템플릿](/jupyter-book/template/template.ipynb)도 준비했습니다.

### 유용한 링크

- [Jupyter Book 문서](https://jupyterbook.org/en/stable/intro.html)
- [MyST 마크다운 문서](https://mystmd.org)
- [Sphinx 문서](https://www.sphinx-doc.org/en/master/)

### 규칙

- 검토를 쉽게 하기 위해 각 문장을 별도의 줄에 배치하십시오.
- 독자가 내용에 압도되지 않도록 드롭다운을 사용하십시오.
- 노이즈를 줄이려면 경고를 생성하지 않는 깔끔한 코드를 작성하고 노트북 시작 시 정보가 없는 경고를 필터링해야 합니다.
- 각 챕터에서 사용된 모든 용어집 용어를 `` {term}`예시 용어` ``로 연결하십시오.
  - 챕터 내에서 각 용어의 **첫 번째 등장**에만 링크하십시오 — 나타날 때마다 링크하지 마십시오.
  - 책 전체에서 여러 번 나타나고 아직 목록에 없는 경우에만 용어집에 새 용어를 추가하십시오. 이 경우 다른 챕터에도 이 용어에 대한 링크를 추가하십시오. 용어가 한 번만 사용되고 불분명할 수 있는 경우 해당 챕터 내에서 직접 설명을 제공하십시오.
  - 용어집 항목과 의미가 같거나 철자가 다른 용어를 연결하려면 다음 형식을 사용하십시오: `` {term}`사용자 용어 <용어집 용어>` `` (예: `` {term}`바코드 <Barcode>` ``).
  - 핵심 내용에는 용어를 연결하지 마십시오!
- 수 시간의 교정 작업 기반: `{cite}` 앞에 항상 공백을 두십시오 (예: ``"이것은 {cite}`Smith2017`에 의해 나타났습니다."``).
- 참고 문헌에는 항상 `doi`와 `url`이 포함되어야 합니다.
- 미국 영어로 작성하십시오.

### 핵심 내용, 환경 및 lamin 드롭다운

환경 및 lamin 드롭다운은 모든 챕터의 제목 뒤에 삽입됩니다. 챕터에 해당 드롭다운을 원하지 않는 경우 `scripts/dropdowns/keytakeaways.py`의 블랙리스트(`black_list_files_yml` 또는 `black_list_files_lamin`)에 노트북을 나열해야 합니다. 핵심 내용 드롭다운은 `<노트북-이름>_keytakeaways.txt`라는 파일이 노트북과 동일한 디렉토리에 있는 경우에만 삽입됩니다. 이 파일에는 다음 형식으로 핵심 내용이 포함되어야 합니다:

```
1
핵심 내용 1의 첫 번째 문장.
핵심 내용 1의 두 번째 문장.

2
핵심 내용 2의 첫 번째 문장.

...
```

핵심 내용을 챕터의 특정 제목에 연결하려면 제목 앞에 `<섹션-이름>-<노트북-이름>-key-takeaway-<핵심-내용-번호>`를 레이블로 추가하십시오. 모든 `_`를 `-`로 바꾸면 핵심 내용의 카드가 텍스트의 제목에 연결됩니다 (예: `(preprocessing-visualization-dimensionality-reduction-key-takeaway-2)=`).

우리의 CI 워크플로우(`.github/worksflows/build_book.yml`)는 책을 빌드할 때 `make dropdown`을 호출합니다. 테스트를 위해 `make` 전에 `make dropdown`을 호출하여 로컬에서 드롭다운을 삽입할 수 있습니다.

> [!WARNING]
> 로컬에서 `make dropdown`을 실행하면 거의 모든 노트북 파일이 수정됩니다. 이러한 변경 사항은 절대로 커밋하거나 리포지토리에 푸시해서는 안 됩니다. `git restore .`를 사용하여 명령을 실행한 직후 이러한 변경 사항을 폐기하는 것이 좋습니다. 원하는 변경 사항을 미리 스테이징했는지 확인하십시오 (`git add`).

### Lamindb

[Lamindb](https://github.com/laminlabs/lamindb)는 계산 생물학에서 대규모 학습을 가능하게 하는 오픈 소스 데이터 프레임워크입니다. 우리는 [theislab/sc-best-practices](https://lamin.ai/theislab/sc-best-practices) 인스턴스를 사용하여 데이터셋과 노트북을 저장, 공유 및 로드하기 위해 lamindb를 사용합니다. [Lamin Labs](https://lamin.ai/)의 무료 호스팅에 감사드립니다.

병합된 기여를 한 경우 `theislab/sc-best-practices` 인스턴스에 추가되도록 요청하십시오. 그런 다음 사용된 모든 데이터셋이 인스턴스에서 직접 로드되는지 확인하십시오. 인스턴스에 새 데이터셋을 업로드하는 경우 별도의 노트북을 만들어 [`scripts`](/scripts/) 폴더에 배치하십시오. [`scripts`](/scripts/) 폴더의 기존 노트북을 가이드로 사용할 수 있습니다. 마지막으로, 노트북을 다시 실행하는 동안 `ln.track()` 및 `ln.finish()`를 사용하여 인스턴스에도 최신 버전을 유지하십시오. [템플릿](/jupyter-book/template/template.ipynb)은 노트북 추적의 기본 단계를 보여줍니다!

> [!Note]
>
> 1. **lamin 계정 만들기**
>
>    - [지침](https://docs.lamin.ai/setup#sign-up-log-in)에 따라 가입하고 로그인하십시오.
>    - `theislab/sc-best-practices` 인스턴스에 추가되도록 요청하십시오.
>
> 2. **lamindb 설치**
>
>    - 환경에 lamindb Python 패키지를 설치하십시오:
>
>    ```bash
>    pip install lamindb[bionty,jupyter,zarr]
>    ```
>
> 3. **[theislab/sc-best-practices 인스턴스](https://lamin.ai/theislab/sc-best-practices)에 연결**
>
>    - `lamin connect` 명령을 실행하십시오:
>
>    ```bash
>    lamin connect theislab/sc-best-practices
>    ```
>
>    - 이제 `→ connected lamindb: theislab/sc-best-practices`가 표시됩니다.
>    - 노트북에서 lamindb를 사용할 준비가 되었습니다!

### 사용자 정의 퀴즈 및 플래시카드 만들기

퀴즈나 플래시카드를 만들려면 `jupyter-book/src/lib.py`의 헬퍼 함수를 사용하십시오. 객관식 문제나 간단한 플립 카드를 만들 수 있습니다.

1. 노트북 코드 셀을 다음으로 시작하십시오

```python
%run ../src/lib.py
```

2. 그런 다음 원하는 만큼 질문을 추가하십시오. 예를 들어:

```python
flip_card("q1", "2 + 2는 무엇인가요?", "4")
multiple_choice_question(
   "q1",
   "프랑스의 수도는 어디인가요?",
   ["파리", "런던", "베를린", "마드리드"],
   "파리",
   {
         "런던": "런던은 영국의 수도입니다",
         "베를린": "베를린은 독일의 수도입니다",
         "마드리드": "마드리드는 스페인의 수도입니다",
   }
)
```

3. 코드 셀을 실행하면 객관식 문제나 플립 카드가 출력으로 생성됩니다.

> [!WARNING]
> 책을 빌드할 때 코드를 제거하려면 코드 셀에 `remove-input` 셀 태그를 추가하십시오.

글꼴 크기, 텍스트 색상 등을 조정할 수도 있습니다. 자세한 내용은 `jupyter-book/src/lib.py`의 메서드 설명을 확인하십시오.

### 사전 커밋

사전 커밋은 커밋하기 전에 마크다운과 코드의 실수를 자동으로 확인하는 도구입니다.

1. `pre-commit`을 설치하십시오:

```bash
pip install pre-commit
```

2. 다음으로, 리포지토리의 루트에서 활성화하십시오:

```bash
pre-commit install
```

3. 그 후에는 언제든지 수동으로 실행할 수 있습니다:

```bash
pre-commit run -a
```

변경 사항을 커밋하려고 하면 오류가 자동으로 확인되고 가능한 경우 수정됩니다. `git add`로 이러한 변경 사항을 커밋에 추가하기만 하면 됩니다.

### `towncrier`로 변경 로그 항목 추가하기

우리는 변경 로그를 관리하기 위해 `towncrier`를 사용합니다. PR을 만들 때 변경 로그 항목을 포함하는 방법은 다음과 같습니다:

1. `towncrier` 설치 (한 번만):

```bash
pip install towncrier
```

2. 평소와 같이 풀 리퀘스트를 만듭니다.

3. PR을 연 후 PR 번호(예: 34)를 기록하고 변경 로그 조각을 만듭니다:

```bash
towncrier create -c '블라블라 업데이트 ([#34](https://github.com/theislab/single-cell-best-practices/pull/34)) <sub>@seohyonkim</sub>' 34.changed.md
```

"블라블라 업데이트"를 변경 사항에 대한 간략한 설명으로, PR 번호를 자신의 PR 번호로, PR 작성자를 자신의 github 태그로 바꾸십시오. `markdown` 파일 이름에 유효한 카테고리는 다음과 같습니다:

`added`
`changed`
`fixed`
`removed`

4. 이렇게 하면 `.md` 파일(예: `34.changed.md`)이 리포지토리 루트의 `changelog.d/` 디렉토리에 생성됩니다. 이 파일이 커밋에 포함되었는지 확인하십시오.

5. 변경 사항을 다시 푸시하십시오.

#### 새 버전 릴리스 (유지 관리자만)

새 버전을 릴리스하려면:

1. Towncrier를 실행하여 변경 로그를 빌드합니다:

```bash
towncrier build --yes --version 2.0.0
```

이렇게 하면 `CHANGELOG.md`가 업데이트되고 `changelog.d/` 디렉토리가 제거됩니다.

2. 생성된 `CHANGELOG.md`의 각 관련 PR 항목 아래에 기여자 이름과 PR 링크를 수동으로 추가합니다.

3. 향후 PR을 위해 `changelog.d/` 디렉토리를 다시 만듭니다:

```bash
mkdir changelog.d
touch changelog.d/.gitkeep
```
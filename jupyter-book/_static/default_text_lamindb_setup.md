이 책은 [lamindb](https://github.com/laminlabs/lamindb)를 사용하여 [theislab/sc-best-practices 인스턴스](https://lamin.ai/theislab/sc-best-practices)를 통해 데이터 세트와 노트북을 저장, 공유 및 로드합니다.
[Lamin Labs](https://lamin.ai/)의 무료 호스팅에 감사드립니다.

1. **lamindb 설치**

   - lamindb 파이썬 패키지를 설치합니다:

   ```bash
   pip install lamindb[bionty,jupyter,zarr]
   ```

2. **선택적으로 lamin 계정 생성**

   - [지침](https://docs.lamin.ai/setup#sign-up-log-in)에 따라 가입하고 로그인합니다.

3. **[theislab/sc-best-practices 인스턴스](https://lamin.ai/theislab/sc-best-practices)에 연결**

   - `lamin connect` 명령을 실행합니다:

   ```bash
   lamin connect theislab/sc-best-practices
   ```

   이제 `→ connected lamindb: theislab/sc-best-practices`가 표시되어야 합니다.

4. **설정 확인**

   - `lamin connect` 명령을 실행합니다:

   ```python
   import lamindb as ln

   ln.Artifact.df()
   ```

   이제 저장된 데이터 세트 중 최대 100개가 표시되어야 합니다.

5. **데이터 세트(아티팩트) 액세스**

   - [아티팩트 페이지](https://lamin.ai/theislab/sc-best-practices/artifacts)에서 데이터 세트를 검색합니다.
   - 아티팩트와 해당 객체를 로드합니다:

   ```python
   import lamindb as ln
   af = ln.Artifact.get(key="key_of_dataset", is_latest=True)  # 또는 ln.Artifact("SOMEID").get()
   obj = af.load()
   ```

   이제 객체가 메모리에서 액세스할 수 있으며 분석할 준비가 되었습니다.
   `ln.Artifact("SOMEID").get()` 접미사를 `ln.Artifact("SOMEID0001").get()`과 같이 수정하여 두 번째 업로드된 버전과 같은 이전 버전을 가져옵니다.

6. **노트북(변환) 액세스**

   - [변환 페이지](https://lamin.ai/theislab/sc-best-practices/transforms)에서 노트북을 검색합니다.
   - 노트북을 로드합니다:

   ```bash
   lamin load <notebook url>
   ```

   그러면 노트북이 현재 작업 디렉토리로 다운로드됩니다.
   `아티팩트`와 유사하게 접미사 ID를 수정하여 이전 버전을 가져올 수 있습니다.

7. **`ln.track()` 및 `ln.finish()` 정보**

   - 이러한 함수는 현재 쓰기 액세스 권한이 있는 사용자만 사용할 수 있으며 오류가 발생할 수 있습니다. 지금은 주석 처리하십시오.
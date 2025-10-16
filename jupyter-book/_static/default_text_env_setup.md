1. **conda 설치**:

   - 환경을 생성하기 전에 시스템에 [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)가 설치되어 있는지 확인하십시오.

2. **yml 내용 저장**:

   - yml 탭의 내용을 `environment.yml`이라는 파일에 복사합니다.

3. **환경 생성**:

   - 터미널 또는 명령 프롬프트를 엽니다.
   - 다음 명령을 실행합니다:
     ```bash
     conda env create -f environment.yml
     ```

4. **환경 활성화**:

   - 환경이 생성되면 다음을 사용하여 활성화합니다:
     ```bash
     conda activate <environment_name>
     ```
   - `<environment_name>`을 `environment.yml` 파일에 지정된 이름으로 바꿉니다. yml 파일에서는 다음과 같이 표시됩니다:
     ```yaml
     name: <environment_name>
     ```

5. **설치 확인**:
   - 다음을 실행하여 환경이 성공적으로 생성되었는지 확인합니다:
     ```bash
     conda env list
     ```
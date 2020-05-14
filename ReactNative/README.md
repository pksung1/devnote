# React Natvie 개발일지

---

## 20200513
- [Async Storage](https://github.com/react-native-community/async-storage)

### 오류

1. Unsupported Modules Detected: Compilation is not supported for following modules: realm. Unfortunately you can't have non-Gradle Java modules and Android-Gradle modules in one project.

2. Invariant Violation: Module AppRegistry is not a registered callabel module (calling runApplication)

--- 

## 20200512
- Daum Map Test
    - [x] DaumMap 연동
    - [x] 주소검색
    - [x] Marker

---

## 20200511

- [react-navigation](https://reactnavigation.org/docs/getting-started)
- [react-native-naver-login](https://github.com/react-native-seoul/react-native-naver-login)
- [react-native-kakao-login](https://github.com/react-native-seoul/react-native-kakao-login)
- [react-native-image-crop-picker](https://github.com/ivpusic/react-native-image-crop-picker)
- [react-native-qrcode-scanner](https://github.com/moaazsidat/react-native-qrcode-scanner)
- [react-native-modal](https://github.com/react-native-community/react-native-modal)
- [react-native-toast](https://github.com/magicismight/react-native-root-toast)
- [google-signin](https://github.com/react-native-community/google-signin)
- [react-native-realm](https://realm.io/docs/javascript/latest/)
- [DaumMap](https://github.com/asata/react-native-daummap)
- 오류
    - Task :app:mergeDexDebug FAILED

---

## 20200507 Toast, Modal, QRCode, Splash, Google Login
- 안드로이드 연결 작업
- Modal 띄우기
    - react-native-modal
- Toast 띄우기
    - ~~react-native-simple-toast~~
    - ~~react-native-easy-toast~~
    - react-native-root-toast
- QRCode 스캔
    - react-native-qrcode-scanner
    - QRCODE Custom
- Splash 화면 만들기
    -  react-native-splash-screen
- Google Signin
- 생긴 버그들
    - SpawnSync adb enoent

---

## 20200506

- 이미지 가져오기
    - ~~Image Picker~~
    - ~~react-native-hooks~~
    - ~~react-native-cameraroll~~
    - react-native-image-crop-picker
- Back Button 컨트롤
- QR코드 스캔 (react-native-qrcode-scanner)
- 하면서 일어난 버그들
    - Cannot fit requested classes in a single dex file
    - Android studio에서 ~1, ~2붙은 중복 모듈이 있는경우
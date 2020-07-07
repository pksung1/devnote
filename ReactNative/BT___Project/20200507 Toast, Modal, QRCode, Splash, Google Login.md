# Todo

20200506
- [x] 이미지 가져오기
- [x] Back Button 컨트롤

20200507 (today)
- [x] 안드로이드 연결 작업
- [x] QR코드스캔 
- [x] Toast 띄우기
- [x] Modal 띄우기
- [x] Splash화면 만들기
- [ ] 다음맵 연결하기
- [ ] 다음맵 주소 검색하기


<hr />

## 안드로이드 연결 작업

개발자모드 -> USB 디버그 모드 킨 후 안드로이드 스튜디오를 통해 설치

```
Could not connect to development server
```
위와같은 오류 발생

https://stackoverflow.com/questions/42064283/could-not-connect-to-react-native-development-server-on-android

```
<application
    android:name="com.example.app"
    android:allowBackup="false"
    android:icon="@mipmap/ic_launcher"
    android:label="@string/app_name"
    android:theme="@style/AppTheme"
    android:usesCleartextTraffic="true">
```
android:usesCleartextTraffic="true" 를 Manifest.xml에 시도함.

<hr />

## Modal 띄우기

[react-native-modal 사용](https://github.com/react-native-community/react-native-modal)

애니메이션은 [react-native-animatable](https://github.com/oblador/react-native-animatable)을 사용했다고 함

<hr />

## Toast 띄우기

[~~react-native-simple-toast~~](https://github.com/xgfe/react-native-simple-toast) 
- Toast 끝난 이후 콜백지원을 하지 않아서 사용안함.

[~~react-native-easy-toast~~](https://github.com/crazycodeboy/react-native-easy-toast) <i>UsedBy: ***2.9k*** Star: ***935***</i>
- 콜백지원
- react의 refs를 이용함
- Toast 커스텀가능
- 커스텀까지는 필요없고 간단한 Toast 기능에 콜백기능이 필요하므로 사용하지않음.

[***react-native-root-toast***](https://github.com/magicismight/react-native-root-toast) <i>UsedBy: ***2.7k*** Star: ***1.4k***</i>
- 콜백지원 (onHidden)
- 시간 설정을 직접 해야함
- 애니메이션도 직접 지정해야함
- 그나마 가장 최근에 업데이트함 *(오늘 기준 12일전 업데이트)*

<hr />

### react-native-root-toast

android에서 Toast가 안나오는 경우가 생김

react-native-root-siblings를 설치 후 Wrapper 생성후 감쌈
```
export default () => {
  // fixer https://github.com/magicismight/react-native-root-siblings/issues/62
  const Wrapper = Platform.OS === 'ios' ? React.Fragment : RootSiblingParent;
  return (
    <Wrapper>
      <App />
    </Wrapper>
  );
};
```
android에서 생기는 문제로 root-siblings로 해결할 수 있다.

<hr />

## QRCode 스캔

[react-native-qrcode-scanner](https://github.com/moaazsidat/react-native-qrcode-scanner)
- 대부분 qrcode-scanner를 사용하는것 같다.

<hr />

### react-native-qrcode-scanner

- IOS 10 이상, Androuid 7이상 따로 설정해줘야 하는것이 있음.
- [react-native-camera](https://github.com/react-native-community/react-native-camera) 가 필요함.

npm install 시 RN버전이 6 이상이므로 link 할 필요가 없고
react-native-camera 설치할땐 따로 [설치 가이드](https://react-native-community.github.io/react-native-camera/docs/installation)를 확인해야함.


#### QRCODE Custom
https://github.com/moaazsidat/react-native-qrcode-scanner/issues/115

누가 예쁘게 커스텀한게 있어서 링크 참조하면 될듯.

사용한건 customMarker, cameraStyle임

<hr />

## Splash 화면 만들기

[react-native-splash-screen](https://github.com/crazycodeboy/react-native-splash-screen)

이거 하나밖에 없는것같다.

---

### react-native-splash-screen

Android, Iphone 따로 만들어줘야 함.

처음에 흰색 화면이 나오는 문제가 있음

어쩔수 없는 문제일수도 있고. 직접 react로 show 함수를 써서 사용하기 때문에 아예 splash컴포넌트를 만드는것도 고민해볼 필요가 있을것같음.

보통은 splash컴포넌트를 만들어서 사용하는것같아보임.

---

## Google Signin

### Usage
[react-native-community/google-signin](https://github.com/react-native-community/google-signin)

### Installed

1. [react-native-community/google-signin](https://github.com/react-native-community/google-signin) 가이드라인대로 설치
    -   [Android](https://github.com/react-native-community/google-signin/blob/master/docs/android-guide.md)
    -   [IOS](https://github.com/react-native-community/google-signin/blob/master/docs/ios-guide.md)

2. Firebase Project 생성, 패키지이름을 맞춰줘야함.

3. 이 프로젝트의 SHA-1 키값을 구해 google-services.json 파일을 얻는다.

4. app 폴더에 넣는다. (gradle 있는곳)

5. Firebase의 Authentication - Sign-in method 에서 구글을 허용한다.

6. webclientId를 이용해 구글로그인을 시도한다.

---

## 생긴 버그들
```
SpawnSync adb enoent
```
https://stackoverflow.com/questions/38835931/react-native-adb-reverse-enoent

export ANDROID_HOME=~/Android/Sdk 로 설정
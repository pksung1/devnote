# ML lec 01 - 기본적인 Machine Learning 의 용어와 개념 설명

## Supervised Learning
- 정해저있는 데이터, 이미 레이블링 된(training set) 데이터로 학습하는방법

## Unsuperviesd Learning
- 일일이 레이블을 정해줄 수 없는것
- 비슷한 단어 찾기 (word clustering)

## Supervised Learning
- image labeling, email spam filter ...

## Training data set
- 정해저있는 x,y 데이터.
- x: 입력값, y: 결과값

## Types of supervised learning
- regression: 0~100 
- binary classification: Pass/NonPass 두가지 경우로 분리
- multi-label classification: A,B,C,D,F 여러가지로 분리

---
# ML lec 02 - Linear Regression의 Hypothesis 와 cost 설명

## Regression

## Hypothesis (가설)

### Linear Hypothesis
- 리니어라 가설을 세움
- H(x) = Wx + b
- 여러 Hypothesis를 해봄

가장 나은걸 확인하는 방법은 cost를 확인하는것

## Cost function
- pow(H(x) - y)

참고: https://hunkim.github.io/ml/lec2.pdf

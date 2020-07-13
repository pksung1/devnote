# [Lodash](https://lodash.com/)

## Lodash란

자바스크립트 유틸리티 라이브러리로 순수함수로 만들어져 있고 배열, 숫자, 객체 문자열 등을 쉽게 처리할수 있도록 도와주는 라이브러리

- Iterating arrays, objects, & strings
- Manipulating & testing values
- Creating composite functions

기본 라이브러리보다 처리가 빠르다.

https://ui.toast.com/weekly-pick/ko_20190515/

---
## 사용해본것들

### [_.cloneDeep(value)](https://lodash.com/docs/4.17.15#cloneDeep)

객체를 모든 dept까지 복사한다. (deep clone)

### [\_.find(collection, [predicate=_.identity], [fromIndex=0])](https://lodash.com/docs/4.17.15#find)

collection의 내부에 데이터를 찾는다. 존재하면 그 데이터를 반환한다.

### [_.isEqual(value, other)](https://lodash.com/docs/4.17.15#isEqual)

value와 other의 값을 비교한다. 같으면 true, 틀리면 false
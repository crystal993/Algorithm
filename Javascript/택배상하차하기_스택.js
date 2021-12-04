// 스택
// - 후입 선출, 가장 늦게 넣은 데이터가 가장 먼저 나가는 것
// - pop 함수 : 배열의 가장 끝 원소를 출력.
// - push 함수 : 배열의 가장 마지막에 원소 삽입.
// - 함수의 반환값
// - 스택 자료구조
// 재고를 택배차에 넣기

재고들 = ["피아노","생수","햇반","아이패드"]
택배차 = []

while (재고들.length) {
    재고 = 재고들.pop()
    택배차.push(재고)
    if (재고들.length == 0) {
        break;
    }
}
console.log(택배차) //'아이패드', '햇반', '생수', '피아노'
//선입 후출
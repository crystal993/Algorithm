// 객체

let 명함 = {
    이름:"김수정",
    나이:26,
    직업:"개발자",
    출력() {
        console.log("이름: "+this.이름)
        console.log(this.이름+"의 직업은 "+this.직업)
    }
}

console.log(명함)
console.log(명함.출력())
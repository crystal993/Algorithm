function 체온계 (ondo) {
    if (ondo > 37.0) {
        console.log("고열입니다.")
    } else if (ondo > 34.0){
        console.log("정상 체온입니다.")
    } else {
        console.log("저체온입니다.")
    }
}

console.log(체온계(37.0))

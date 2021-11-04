loadFile = () =>{
    var selectedFile = document.getElementById("openFile").files[0];//获取读取的File对象
    var name = selectedFile.name;//读取选中文件的文件名
    var size = selectedFile.size;//读取选中文件的大小
    //console.log("文件名:"+name+"大小："+size);
    var reader = new FileReader();//这里是核心！！！读取操作就是由它完成的。
    reader.readAsText(selectedFile);//读取文件的内容
    reader.onload = function(){
        //console.log("读取结果：", this.result);//当读取完成之后会回调这个函数，然后此时文件的内容存储到了result中。直接操作即可。
        //console.log("读取结果转为JSON：");
        let json = JSON.parse(this.result);
        //console.log(json.name);
        console.log("nmsl");
        var httpRequest = new XMLHttpRequest();//第一步：创建需要的对象
        httpRequest.open('POST', 'http://127.0.0.1:8000/load_file', true); //第二步：打开连接/***发送json格式文件必须设置请求头 ；如下 - */
        httpRequest.setRequestHeader("Content-type","application/json");//设置请求头 注：post方式必须设置请求头（在建立连接后设置请求头）var obj = { name: 'zhansgan', age: 18 };
        httpRequest.send(JSON.stringify(json));//发送请求 将json写入send中
        var arrayRouterAdress=[];
        var arrayRouterName=[];
        //json.router.forEach((each_router=>{
        //    console.log(each_router)
        //}))
    };
}
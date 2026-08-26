# GOTO将传递参数返回值保存到变量，脚本参数回调

GOTO将传递参数返回值保存到变量，脚本参数回调





[@run]
#act
goto @test(1,2|N$返回值1,S$返回值2)
sendmsg 7 ...<$str(N$返回值1)>,<$str(S$返回值2)>

[@test]
#act
formulation <$scriptparam1>\*2 N$计算结果1
formulation <$scriptparam2>\*2 N$计算结果2
MOV S$计算结果 参数2返回值：<$str(N$计算结果2)>
return <$str(N$计算结果1)> <$STR(S$计算结果)>
;return返回N个参数保存到上面指定变量中，注意return等同break，脚本段使用return下方不再执行..
sendmsg 7 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

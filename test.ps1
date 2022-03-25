$lang = $args[0]
$problem_num = $args[1]
$testcase_num = $args[2]


switch ($lang) {
    py {  python ".\python\test_runner.py" $problem_num $testcase_num }
    cs {  Write-Output "5678"  }
    default { Write-Output "language not specified" }
}
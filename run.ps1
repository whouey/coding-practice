$lang = $args[0]
$problem_num = $args[1]


switch ($lang) {
    py {  python ".\python\test_runner.py" $args[1] $args[2] }
    cs {  Write-Output "5678"  }
    default { Write-Output "language not specified" }
}
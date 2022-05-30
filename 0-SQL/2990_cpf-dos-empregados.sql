SELECT empregados.cpf, empregados.enome, departamentos.dnome
FROM departamentos
INNER JOIN empregados
ON departamentos.cpf_gerente = empregados.cpf
ORDER BY empregados.cpf;
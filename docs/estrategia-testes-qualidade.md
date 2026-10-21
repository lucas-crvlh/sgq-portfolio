# Estratégia de testes e qualidade — SGQ Portfolio

**Status:** catálogo mínimo implementado com testes locais; cenários de revisões, avaliações e auditoria permanecem planejados. Foram executados **12 testes com sucesso no ambiente local**; o workflow do GitHub Actions está configurado para executar a suíte automaticamente. Consulte as execuções para verificar o resultado de CI.  
**Abrangência:** código próprio e dados inteiramente sintéticos.  
**Natureza:** proposta independente para portfólio, sem replicar planos de teste, artefatos ou políticas da empresa confidencial.

## 1. Objetivo

Registrar como o catálogo inicial é validado e como os demais módulos demonstrativos serão testados conforme forem implementados. O foco é mostrar decisões de engenharia verificáveis: **comportamento correto, autorização no backend, consistência transacional e rastreabilidade**.

O cenário de referência é fictício: o documento `DOC-DEMO-001` aparece cadastrado como `R1`; uma verificação simulada encontra `R2`; um usuário autorizado registra uma avaliação com justificativa e o histórico permanece consultável.

Os cenários PORT-T01 a PORT-T03 já possuem testes implementados em [tests/test_catalogo.py](../tests/test_catalogo.py), com execução local de 12 testes aprovada. Os demais cenários representam **critérios planejados**, não evidências de aprovação.

## 2. Abordagem por nível

| Nível | Finalidade | Ferramentas candidatas |
| --- | --- | --- |
| Unitário | Verificar validações, invariantes e transições de estado isoladas | Python, Pytest |
| Integração | Verificar serviços, repositórios e persistência em transações | Pytest, banco de teste descartável |
| API / contrato | Validar entradas, respostas, autenticação e autorização HTTP | FastAPI TestClient ou HTTPX, Pytest |
| Interface | Verificar os fluxos críticos do usuário quando existir frontend | Framework de teste a definir |
| Segurança / regressão | Exercitar negação de acesso, dados inválidos, regressões e dependências | Pytest e verificações automatizadas a definir |

A proposta é concentrar a maior parte das verificações em testes rápidos de unidade e de API, mantendo poucos testes de ponta a ponta para fluxos realmente críticos.

## 3. Matriz de cenários prioritários

Os identificadores `PORT-Txx` existem **apenas neste portfólio** e não correspondem a tickets, cenários ou documentos internos.

| ID | Cenário planejado | Tipo | Resultado esperado |
| --- | --- | --- | --- |
| PORT-T01 | Criar referência fictícia válida e consultar por identificador | API / integração | Registro criado e retornado corretamente |
| PORT-T02 | Tentar cadastrar identificador duplicado | Domínio / API | Operação recusada; nenhum novo registro inconsistente |
| PORT-T03 | Enviar campos obrigatórios ausentes ou inválidos | API | Erro de validação; nenhuma gravação parcial |
| PORT-T04 | Registrar verificação que identifica `R2` para `DOC-DEMO-001` | Integração | Verificação e vínculo com documento preservados |
| PORT-T05 | Usuário somente leitura tenta concluir avaliação | Autorização / API | Ação negada pelo backend; estado inalterado |
| PORT-T06 | Usuário autorizado registra avaliação com justificativa | Integração | Avaliação e registro auditável vinculados à ação |
| PORT-T07 | Solicitação de avaliação sem justificativa obrigatória | Domínio / API | Operação recusada segundo contrato definido |
| PORT-T08 | Falha simulada durante operação que exige histórico | Integração | Transação revertida; sem estado parcialmente confirmado |
| PORT-T09 | Consulta ao histórico da referência | API / integração | Eventos vinculados à referência consultada em ordem definida |
| PORT-T10 | Tentativas repetidas de uma mesma operação sensível | Integração | Comportamento idempotente ou conflito explícito, conforme contrato futuro |

**Implementados neste incremento:** PORT-T01 a PORT-T03 (incluindo validação e persistência), com testes adicionais de paginação e reinício. **Planejados:** PORT-T04 a PORT-T10, dependentes de futuras funcionalidades. A suíte executada possui **12 casos de teste parametrizados incluídos**.

## 4. Dados e isolamento

- Utilizar apenas referências, usuários e eventos fictícios.
- Criar estados iniciais determinísticos por fixture, sem dependência da ordem de execução.
- Isolar testes e restaurar os dados entre cenários.
- Executar testes de persistência em banco descartável, sem conexões com ambientes corporativos.
- Não incluir tokens, credenciais, identificadores internos, planilhas reais ou documentos técnicos licenciados.
- Não usar dados de produção, mesmo que parcialmente anonimizados.

## 5. Critérios de aceite e evidências

Uma funcionalidade da **demonstração pública** só deverá ser marcada como implementada depois de:

1. Existir código próprio no repositório e instruções de execução local.
2. Ter seus comportamentos e erros documentados.
3. Possuir testes automatizados proporcionais ao risco e ao escopo implementado.
4. Ter resultados de execução reproduzíveis e rastreáveis a um commit.
5. Ser revisada quanto à ausência de dados confidenciais e dependências desnecessárias.

A evidência deverá apontar para testes e execuções existentes. Não serão publicados percentuais de cobertura, contagens de testes, badges de CI ou alegações de segurança sem medição correspondente.

## 6. Integração contínua implementada

O arquivo [`.github/workflows/ci.yml`](../.github/workflows/ci.yml) define a execução dos testes Python no GitHub Actions.

```text
Push na main / Pull request para main / Execução manual
        |
        v
Runner ubuntu-24.04 + Python 3.12
        |
        v
Instalar dependências fixadas em requirements.txt
        |
        v
Conferir consistência das dependências (pip check)
        |
        v
Executar suíte: python -m pytest -q
        |
        v
GitHub Actions registra sucesso/falha do job
```

A automação utiliza permissões mínimas de leitura (`contents: read`), não precisa de secrets e executa os testes com base em arquivos temporários SQLite. O checkout desabilita a persistência de credenciais.

**Limites:** este workflow não configura lint, cobertura, testes de interface, varredura de segurança ou verificação de código confidencial. Nenhum desses controles deve ser tratado como implementado.

**Evidência:** resultados devem ser verificados na [página de execuções do GitHub Actions](https://github.com/lucas-crvlh/sgq-portfolio/actions/workflows/ci.yml) e associados ao commit testado. A criação do workflow não constitui, por si só, evidência de aprovação.

## 7. Riscos considerados

| Risco | Verificação proposta |
| --- | --- |
| Usuário sem permissão altera uma avaliação | Testes negativos de autorização no backend |
| Alteração salva sem histórico correspondente | Testes de transação e rollback |
| Referência duplicada compromete a consistência | Testes de duplicidade e integridade |
| Entrada inválida alcança regras críticas | Testes de validação de contrato |
| Refatoração altera comportamento existente | Testes de regressão por caso de uso |
| Exemplo público revela informações internas | Revisão de confidencialidade antes de cada publicação |

## 8. Escopo deliberadamente não afirmado

Este documento **não certifica conformidade normativa, segurança, capacidade de produção ou qualidade do sistema corporativo original**. O incremento de catálogo possui testes locais e workflow de CI configurado, mas ainda não dispõe de controle de acesso nem cobertura para os módulos futuros.

À medida que novos módulos e testes forem implementados, esta matriz deverá ser atualizada com links para código, comandos de execução e resultados correspondentes.

---

Documento preparado exclusivamente para o **SGQ Portfolio**, com exemplos fictícios e sem artefatos proprietários.

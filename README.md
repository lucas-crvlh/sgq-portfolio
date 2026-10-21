# SGQ — Sistema de Gestão da Qualidade

[![Python tests](https://github.com/lucas-crvlh/sgq-portfolio/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/lucas-crvlh/sgq-portfolio/actions/workflows/ci.yml)

**Portfólio técnico | Engenharia de Software | Gestão de Normas Técnicas**

Este repositório documenta uma **versão demonstrativa e independente** de um Sistema de Gestão da Qualidade (SGQ), inspirada em desafios de engenharia de software enfrentados em um projeto para uma **empresa confidencial**.

O sistema corporativo original e seu repositório são privados. O conteúdo aqui publicado será desenvolvido especificamente para fins de portfólio, com exemplos fictícios, sem reutilizar código, documentos ou dados internos.

## Resumo executivo

| Aspecto | Visão geral |
| --- | --- |
| **Problema** | Dependência de controles manuais para acompanhar documentos técnicos, suas revisões e as decisões associadas. |
| **Solução de referência** | Sistema corporativo de gestão de normas técnicas com organização do acervo, rastreabilidade e fluxos de avaliação humana. |
| **Engenharia no contexto profissional** | APIs e aplicação web com Python, FastAPI, React, TypeScript e PostgreSQL; arquitetura de monólito modular, testes e controles de acesso. |
| **Demonstração pública** | Catálogo fictício independente com FastAPI, SQLAlchemy, SQLite, 12 testes automatizados e GitHub Actions. Não reproduz o sistema corporativo. |
| **Confidencialidade** | Empresa não identificada, repositório original privado e exemplos sintéticos. |

## Minha atuação

Minha participação profissional neste projeto incluiu atividades de **análise de sistemas, engenharia de software e organização das entregas técnicas**:

- **Discovery e requisitos:** investigação de processos manuais, levantamento de necessidades e definição do escopo inicial de gestão de normas técnicas.
- **Modelagem e arquitetura:** organização das regras de negócio, fluxos de informação, responsabilidades dos módulos e decisões técnicas.
- **Desenvolvimento:** implementação e evolução de componentes da aplicação, APIs e persistência, em colaboração com as áreas envolvidas.
- **Qualidade e rastreabilidade:** validação técnica, testes automatizados, documentação de mudanças e acompanhamento das entregas por versionamento e revisão de código.

As decisões de negócio, os critérios de Qualidade e as aprovações funcionais permanecem com os respectivos responsáveis. Esta descrição apresenta **minha contribuição**, não atribui a mim individualmente todas as entregas da equipe.

**Neste repositório público**, desenvolvi e documentei separadamente a demonstração do catálogo, seus testes e a integração contínua, usando apenas código original e dados fictícios.

> **Status:** primeiro incremento executável do catálogo fictício (API para cadastro, listagem e consulta, com persistência local e testes). Os demais módulos, incluindo verificações, avaliações, RBAC e auditoria, permanecem **planejados** e não estão implementados.

## Visão geral

A gestão de normas técnicas envolve identificação de documentos, acompanhamento de revisões, registro de verificações e análise do impacto de mudanças. Em processos baseados em planilhas e conferências manuais, a rastreabilidade das informações e decisões pode se tornar complexa.

A proposta desta demonstração é explorar como uma aplicação centralizada pode apoiar essas atividades, mantendo **histórico auditável, permissões por responsabilidade e validação humana**.

## Estudo de caso técnico (cenário fictício)

### Problema

Considere uma equipe responsável por acompanhar referências técnicas utilizadas em suas atividades. Quando a revisão de um documento muda, é necessário identificar a diferença, avaliar sua relevância, registrar uma decisão e preservar evidências do processo. Registros dispersos dificultam a consulta ao histórico e a identificação de pendências.

### Exemplo demonstrativo

O cenário abaixo é **inteiramente sintético**. Não descreve documentos, decisões, prazos ou procedimentos internos da empresa confidencial.

| Campo | Valor fictício |
| --- | --- |
| Referência | `DOC-DEMO-001` |
| Documento | Procedimento técnico ilustrativo |
| Revisão cadastrada | `R1` |
| Revisão identificada na simulação | `R2` |
| Situação ilustrativa | Alteração a avaliar |
| Responsável pela avaliação | Usuário fictício com permissão de análise |

### Fluxo proposto

```text
Referência cadastrada (R1)
          |
          v
Verificação simulada identifica R2
          |
          v
Registro de divergência e evidência fictícia
          |
          v
Pendência para análise por pessoa autorizada
          |
          v
Decisão humana com justificativa
          |
          v
Histórico consultável da verificação e da decisão
```

Neste exemplo, o software **organiza informações e registra ações**, mas **não decide automaticamente** se uma revisão deve ser adotada.

### Aspectos de engenharia demonstráveis

- **Modelagem de domínio:** separar documentos, revisões, verificações, pendências e registros de auditoria.
- **Regras de acesso:** permitir que somente perfis autorizados registrem avaliações e decisões.
- **Integridade e rastreabilidade:** vincular cada evento à referência analisada, ao usuário fictício e ao instante do registro.
- **API e persistência:** prever contratos de leitura e escrita, com validações e histórico consistente.
- **Estratégia de testes:** exercitar permissões, entradas inválidas, transições de estado e preservação do histórico.

**Estado de implementação:** este estudo de caso permanece ilustrativo quanto ao fluxo de verificações, avaliações e auditoria. Apenas o **catálogo mínimo de normas fictícias** possui API, armazenamento e testes implementados. Não há interface gráfica nem as demais etapas do fluxo.

## Escopo previsto para a demonstração

| Módulo | Objetivo |
| --- | --- |
| Catálogo de normas | **Implementado parcialmente:** cadastrar, listar e consultar referências fictícias, com SQLite local. |
| Acompanhamento de revisões | Registrar verificações, versões e evidências simuladas. |
| Análise de impacto | Organizar pendências e avaliações por responsáveis autorizados. |
| Histórico auditável | Registrar alterações, autoria, data e justificativa. |
| Controle de acesso | Restringir ações conforme o perfil de usuário. |
| Indicadores | Visualizar pendências e estados de acompanhamento. |

## Arquitetura de referência

A demonstração adotará, como referência, uma abordagem de **monólito modular**: uma aplicação com responsabilidades separadas por domínio e implantação simplificada.

```text
Interface web
    |
    v
API de aplicação
    |
    +-- Catálogo de normas
    +-- Acompanhamento de revisões
    +-- Análise de impacto
    +-- Auditoria e permissões
    |
    v
Banco de dados relacional
```

**Stack implementada neste incremento:** Python, FastAPI, SQLAlchemy, SQLite e Pytest. React, PostgreSQL e Docker são possibilidades futuras, **não componentes implementados**.

Consulte [Decisões arquiteturais da demonstração](docs/decisoes-arquiteturais.md) para a justificativa do monólito modular, os limites de cada camada e os trade-offs considerados.

Consulte também [Estratégia de testes e qualidade](docs/estrategia-testes-qualidade.md) para os cenários implementados e planejados, critérios de aceite e abordagem de validação. Os testes do catálogo estão implementados; revisões, avaliações, RBAC e auditoria continuam planejados.

## Primeiro incremento executável: catálogo fictício

Implementado de forma independente para fins de portfólio, sem código ou dados corporativos.

| Método | Endpoint | Operação | Respostas principais |
| --- | --- | --- | --- |
| `GET` | `/health` | Verificar disponibilidade da API | `200` |
| `POST` | `/normas` | Cadastrar norma fictícia | `201`, `409` duplicado, `422` inválido |
| `GET` | `/normas` | Listar normas, com `limit` e `offset` | `200`, `422` |
| `GET` | `/normas/{codigo}` | Consultar por código | `200`, `404` |

**Execução local** (Python 3.11+):

```bash
git clone https://github.com/lucas-crvlh/sgq-portfolio.git
cd sgq-portfolio
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Com o servidor ativo, acesse `http://127.0.0.1:8000/docs` para experimentar os endpoints via Swagger UI. Exemplo de corpo para `POST /normas`:

```json
{
  "codigo": "DEMO-NORMA-001",
  "titulo": "Documento demonstrativo de medição",
  "revisao": "R1",
  "organismo_emissor": "Organismo Fictício"
}
```

A aplicação cria o arquivo local `sgq_portfolio.db` automaticamente; ele é ignorado pelo Git.

**Testes:**

```bash
python -m pytest -q
```

**Resultado de validação local:** 12 testes aprovados no desenvolvimento do incremento. Os testes exercitam criação, leitura, normalização, duplicidade, validação, paginação e persistência após reinício.

**Integração contínua:** [GitHub Actions — Python tests](https://github.com/lucas-crvlh/sgq-portfolio/actions/workflows/ci.yml) executa `python -m pytest -q` em pull requests, pushes na `main` e acionamento manual. Consulte o histórico do workflow para confirmar os resultados de execução no GitHub; a presença do arquivo, isoladamente, não comprova aprovação.

**Limitações:** este protótipo não implementa autenticação, RBAC, auditoria, acompanhamento de revisões ou decisões. Por isso, **destina-se exclusivamente a estudo e execução local; não deve ser exposto publicamente como serviço**.

## Princípios técnicos

- **Rastreabilidade:** associar informações a suas fontes e aos registros que as fundamentam.
- **Auditabilidade:** permitir compreender quem realizou cada ação e por quê.
- **Segurança:** aplicar controle de acesso conforme permissões definidas.
- **Validação:** apoiar a conferência técnica sem automatizar decisões que exigem julgamento humano.
- **Manutenibilidade:** separar responsabilidades e manter interfaces testáveis.
- **Qualidade:** documentar comportamentos e verificar regras com testes automatizados.

## Limites da publicação

Esta versão de portfólio **não é um clone, fork ou distribuição do SGQ corporativo**.

- Nenhum código-fonte, histórico Git ou configuração do sistema original será publicado.
- Dados, usuários, documentos, telas e fluxos de exemplo serão fictícios ou criados do zero.
- A identificação da organização e os detalhes internos de sua operação permanecerão confidenciais.
- Qualquer componente executável futuro terá implementação independente e documentação própria.

## Próximas etapas

O catálogo mínimo de normas fictícias já possui API, persistência SQLite, testes automatizados e workflow de integração contínua no GitHub Actions. Próximos incrementos poderão ampliar as funcionalidades, começando pela análise das lacunas do catálogo. Toda evolução deverá usar código próprio e dados sintéticos, com registro explícito das funcionalidades realmente implementadas.

---

**Responsável pelo portfólio:** [Lucas Carvalho Cordeiro](https://github.com/lucas-crvlh)  
**Contato:** [LinkedIn](https://www.linkedin.com/in/lucas-crvlh00/)

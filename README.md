# SGQ — Sistema de Gestão da Qualidade

**Portfólio técnico | Engenharia de Software | Gestão de Normas Técnicas**

Este repositório documenta uma **versão demonstrativa e independente** de um Sistema de Gestão da Qualidade (SGQ), inspirada em desafios de engenharia de software enfrentados em um projeto para uma **empresa confidencial**.

O sistema corporativo original e seu repositório são privados. O conteúdo aqui publicado será desenvolvido especificamente para fins de portfólio, com exemplos fictícios, sem reutilizar código, documentos ou dados internos.

> **Status:** documentação conceitual inicial. Ainda não há uma aplicação demonstrativa executável neste repositório. Os recursos descritos abaixo representam o escopo da demonstração pública, não funcionalidades já entregues aqui.

## Visão geral

A gestão de normas técnicas envolve identificação de documentos, acompanhamento de revisões, registro de verificações e análise do impacto de mudanças. Em processos baseados em planilhas e conferências manuais, a rastreabilidade das informações e decisões pode se tornar complexa.

A proposta desta demonstração é explorar como uma aplicação centralizada pode apoiar essas atividades, mantendo **histórico auditável, permissões por responsabilidade e validação humana**.

## Escopo previsto para a demonstração

| Módulo | Objetivo |
| --- | --- |
| Catálogo de normas | Cadastrar e consultar referências técnicas fictícias. |
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

**Stack considerada para a versão pública:** Python, FastAPI, React, PostgreSQL, Docker e Pytest. A implementação e as escolhas técnicas efetivas serão documentadas conforme forem realizadas.

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

A primeira implementação planejada é um catálogo mínimo de normas fictícias, acompanhado de API, persistência, testes e instruções de execução. O escopo poderá evoluir incrementalmente, com registro explícito do que estiver realmente implementado.

---

**Responsável pelo portfólio:** [Lucas Carvalho Cordeiro](https://github.com/lucas-crvlh)  
**Contato:** [LinkedIn](https://www.linkedin.com/in/lucas-crvlh00/)

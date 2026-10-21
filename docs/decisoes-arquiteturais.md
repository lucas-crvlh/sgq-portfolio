# Decisões arquiteturais — SGQ Portfolio

**Status:** proposta de arquitetura para demonstração pública; não implementada.  
**Escopo:** projeto independente com dados fictícios.  
**Nota de confidencialidade:** este documento foi redigido especificamente para o portfólio. Não reproduz especificações, diagramas, código nem decisões registradas no repositório corporativo.

## Objetivo

Documentar as escolhas técnicas previstas para um protótipo de gestão de normas, revisões e avaliações humanas. As decisões a seguir são **propostas para este repositório**, não uma descrição verificável da implementação original.

## DA-001 — Monólito modular no backend

**Decisão proposta:** desenvolver uma única aplicação backend, dividida em módulos com responsabilidades definidas.

**Motivos:**
- O domínio da demonstração é pequeno e seus fluxos possuem dependências entre si.
- Uma implantação única simplifica desenvolvimento, depuração e testes de integração.
- Operações que alteram documentos e registram eventos de auditoria podem compartilhar transações locais.
- A modularização permite evolução gradual sem introduzir comunicação distribuída prematuramente.

**Alternativas consideradas:**
- **Microsserviços:** maior independência de implantação, mas adicionam comunicação entre serviços, observabilidade distribuída e tratamento de falhas de rede; custo pouco justificável para este protótipo.
- **Monólito sem separação interna:** menor esforço inicial, porém tende a aumentar o acoplamento entre regras, acesso a dados e endpoints.

**Trade-off:** a aplicação será implantada e escalada como uma unidade. Caso limites de domínio e necessidades operacionais mudem, a arquitetura poderá ser reavaliada com evidências.

> "Monólito modular" refere-se à **organização do backend**. A interface web e o banco de dados continuam componentes distintos, o que não torna a arquitetura de microsserviços.

## DA-002 — Responsabilidades por camada

**Decisão proposta:** separar apresentação, transporte HTTP, aplicação, domínio e persistência. O diagrama é ilustrativo e não descreve a estrutura de diretórios de um sistema existente.

```text
Interface web (React, proposta)
             |
             | HTTP / JSON
             v
API REST (FastAPI, proposta)
             |
             v
Casos de uso / aplicação
             |
       +-----+-------------------------+
       |              |                |
  Catálogo       Verificações      Avaliações
       +--------------+----------------+
                      |
              Regras de domínio
                      |
               Repositórios
                      |
             PostgreSQL (proposta)

Autorização e auditoria: preocupações transversais
```

| Camada | Responsabilidade prevista | Não deve assumir |
| --- | --- | --- |
| Interface | Exibir dados e coletar ações do usuário | Autorizar decisões críticas por conta própria |
| API | Validar contratos HTTP e encaminhar requisições | Concentrar regras de domínio complexas |
| Aplicação | Orquestrar casos de uso e limites transacionais | Acoplar regras à interface |
| Domínio | Definir invariantes e transições válidas | Depender de detalhes do framework web |
| Persistência | Consultar e armazenar entidades | Decidir o resultado de avaliações técnicas |
| Auditoria e autorização | Verificar permissões e registrar ações relevantes | Substituir a decisão humana |

**Critério de avaliação futuro:** conseguir testar uma regra de domínio sem iniciar a interface web e verificar um caso de uso com persistência de teste.

## DA-003 — Persistência relacional e histórico

**Decisão proposta:** utilizar banco relacional para representar entidades relacionadas e garantir consistência entre registros.

No cenário fictício `DOC-DEMO-001`, uma verificação que indica a revisão `R2` poderá gerar uma pendência de avaliação. A proposta é registrar a ação relevante e seu contexto dentro da mesma unidade transacional, sempre que aplicável.

**Razões:** integridade referencial, suporte a transações e consultas que relacionam documento, revisão, pendência, responsável e histórico.

**Cuidados de desenho:** registrar autoria e instante; evitar exclusões que destruam evidências; não confundir status do documento com conclusão da avaliação. A estratégia específica de retenção e imutabilidade ainda precisa ser definida na implementação demonstrativa.

## DA-004 — Autoridade humana e controle de acesso

**Decisão proposta:** automatizar registro e organização, mas reservar a conclusão de avaliações técnicas a usuários autorizados.

- Aplicar autorização no backend, independentemente da visibilidade de botões na interface.
- Diferenciar permissão de leitura da permissão de registrar avaliações.
- Exigir justificativas onde a decisão afetar a rastreabilidade.
- Tratar integrações e análises automáticas futuras como apoio, não como aprovação autônoma.

O protótipo poderá usar **perfis fictícios** para demonstrar RBAC (*Role-Based Access Control*, controle de acesso por papéis).

## Validação planejada

Antes de declarar qualquer capacidade como implementada, a versão pública deverá demonstrar, com código e testes próprios:

1. Contratos de API e validação de entradas.
2. Restrições de autorização nos casos de uso protegidos.
3. Consistência entre criação de pendências e registros de histórico.
4. Tratamento de tentativas inválidas e transições de estado não permitidas.
5. Execução reproduzível localmente com dados exclusivamente sintéticos.

## Limitações

Nenhuma das decisões acima comprova funcionalidade operacional neste repositório. Tecnologias, módulos, endpoints, políticas e testes poderão mudar durante a implementação; alterações relevantes deverão ser registradas neste documento.

Este material não permite inferir os controles efetivos, a infraestrutura ou o nível de maturidade do sistema corporativo de origem.

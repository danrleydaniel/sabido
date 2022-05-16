Histórico de revisões  
| Data | Versão | Descrição | Autor |  
| --- | --- | --- | --- |
| 02/05/2022 | 1.0 | Documento inicial | Gabriel e Douglas |  


# Equipe e Definição de Papéis
| Equipe | Papel | E-mail |  
| --- | --- | --- |
| Danrley | Gerente | danrleydaniel21@gmail.com
| Douglas | Desenvolvedor | douglasmateus1@hotmail.com
| Ednalda | Desenvolvedor | edinaldacrist@hotmail.com
| Gabriel Azevedo | Desenvolvedor | gabrielazevedo492@gmail.com
| Gabriel Gonçalo | Desenvolvedor | gabriel.tchutcha@hotmail.com.br
| Lucas | Desenvolvedor | santoslucas9956@gmail.com

# Descrição do projeto

SABIDO é um aplicativo desenvolvido com o objetivo de ajudar os estudantes a organizarem suas tarefas e rotinas, além de ter funções que auxiliam o estudante no controle de seu desempenho acadêmico.  

# Perfis dos Usuários

Estudantes de qualquer etapa de ensino, seja fundamental, médio, superior.

## Perfil Aluno

Este usuário utiliza o sistema para verificar seus compromissos, seu desempenho acadêmico (Histórico de disciplinas já cursadas e que estão sendo cursadas atualmente), saber de quanto precisa na prova final (Para repor uma nota).

# Requisitos Funcionais

## RF01 - Incluir Aluno

Descrição: A inclusão de um aluno (Cadastro) solicita os atributos matricula, nome, endereço, email, celular, instituição em que estuda, login, senha, etc.

Ator: Aluno

## RF02 - Alterar Aluno

Descrição: A alteração de um aluno permite a mudança (Atualização) dos dados já armazenados referentes às informações pessoais do aluno, como mudança de email, número de celular, login, senha, etc.

Ator: Aluno

## RF03 - Visualizar Meus dados pessoais

Descrição: Permite o aluno vizualizar o próprio perfil com os dados pessoais.

Ator: Aluno

## RF04 - Listar todos os alunos

Descrição: Visualizar uma lista com todos os alunos que estão cadastrados no sistema.

Ator: Administrador

## RF05 - Visualizar Aluno específico

Descrição: Visualizar os dados de um determinado aluno.

Ator: Administrador

## RF06 - Excluir Aluno

Descrição: Se socilitado, o administrador pode excluir os dados de um determinado aluno.

Ator: Administrador

## RF07 - Incluir Disciplina

Ator: Aluno

Descrição: A inclusão de uma disciplina solicita os dados Nome da disciplina, Professor da disciplina, Carga horária da disciplina, Código da disciplina, etc.

## RF09 - Alterar Disciplina

Descrição: Alterar informações sobre uma determinada disciplina.

Ator: Aluno

## RF10 - Visualizar Disciplina

Descrição: Visualizar informações sobre uma determinada disciplina.

Ator: Aluno

## RF11 - Excluir Disciplina

Descrição: O aluno pode excluir uma determinada disciplina do seu histórico.

Ator: Aluno

## RF12 - Histórico de Disciplinas

Descrição: Exibe um relatório de todas as disciplinas já cursadas no passado e que estão sendo cursadas no presente pelo aluno, permite o estudante consultar o seu histórico de notas por unidade em cada disciplina e a sua situação (Aprovado / Reprovado / Aprovado por Nota.

Ator: Aluno

## RF13 - Calculadora simuladora de resultado

Descrição: Permite o aluno estimar a nota mínima que precisa para ser aprovado em determinada disciplina com a inserção das notas por unidades para cada disciplina cursada e a atribuição de pesos por unidades.

Autor: Aluno

## RF14 - Gerar Horário de Aulas 

Descrição: Baseado nas disciplinas que estão sendo cursadas no momento, agrupa-las por dia, turno e hora da aula.

Autor: Aluno

## RF14 - Incluir Compromisso

Descrição: A inclusão de um compromisso solicita os atributos Nome do compromisso, Descrição, Nome da disciplina, Data do compromisso.

Ator: Aluno

## RF15 - Alterar Compromisso

Descrição: A alteração de um aluno permite a mudança (Atualização) dos dados já armazenados referentes aos compromissos.
Ator: Aluno

## RF16 - Visualizar Meus Compromissos

Descrição: Permite o aluno vizualizar uma lista com todos os compromissos em que ele está submetido.

Ator: Aluno

## RF18 - Visualizar Compromisso específico

Descrição: Visualizar as informações de um determinado compromisso.

Ator: Aluno

## RF19 - Excluir Compromisso

Descrição: Excluir um determinado compromisso manualmente ou após o seu prazo ter se expirado.

Ator: Aluno

# Requisitos não-Funcionais

## RNF01 - Persistência de dados 

Descrição: Ao excluir um aluno, deve ser realizada uma Exclusão Lógica, de modo a apenas ocultar tal usuário do sistema, mas não deletar definitivamente suas informações (Apenas se o próprio aluno exigir isso).

## RNF02 - Responsividade multiplataforma

Descrição: O aplicativo deve ser multiplataforma (Computadores, Tablets e Celulares), portanto a responsividade deve ser assegurada.

## RNF03 - Notificações 

Descrição: O aluno pode optar por receber lembretes por email sobre determinado compromisso, podendo escolher ser lembrado a cada dia ou apenas quando estiver faltando uma semana para o prazo final.

## RNF04 - Interface intuitiva

Descrição: O aplicativo deve ter uma interface amigável, de modo que o mesmo possa ser de fácil compreensão e de fácil usabilidade até mesmo para jovens alunos do ensino fundamental.


# Riscos

| Data | Risco | Prioridade | Responsável | Status | Providência/solução |  
| --- | --- | --- | --- | --- | ---|
| 02/05/2022 | Não aprendizado das ferramentas utilizadas para o desenvolvimento do projeto | Média | Todos | Vigente | Estudar a fundo as ferramentas e assistir tutoriais sobre as ferramentas.| 
| 02/05/2022 | Falta de disponibilidade de algum dos integrantes do projeto | Média | Todos | Vigente | Organizar um tempo para dedicação ao desenvolvimento do projeto
| 02/05/2022 | Não cumprir todos as issues antes da data da entrega de cada tarefa | Baixa | Gerente | Vigente | Solicitar aos desenvolvedores que completem as issues até a data de cada tarefa
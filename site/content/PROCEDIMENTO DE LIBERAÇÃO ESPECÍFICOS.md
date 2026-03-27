# PROCEDIMENTO DE LIBERAÇÃO ESPECÍFICOS

PROCEDIMENTO DE LIBERAÇÃO ESPECÍFICOS\- CAMIL

1 \- Solicitação de fontes específicos

Os fontes mantidos no ARACAGI e/ou AZURE/TFS da Totvs deve ser utilizado somente para consulta e pesquisa\. Para manutenção e/ou melhoria é necessário solicitar via e\-mail, conforme exemplo abaixo, ao Luciano Mengarda \(luciano\.mengarda@dwcconsult\.com\.br\) os fontes atualizados no AZURE da Camil\. Na ausência do Luciano Mengarda, a solicitação deverá ser feita para Gabriel Shiratori \([gabriel\.shiratori@totvs\.com\.br](mailto:gabriel.shiratori@totvs.com.br)\)\.

Exemplo solicitação de fontes:

__*Assunto: Solicitação de fontes \- CAMIL*__

__*Bom dia Luciano,*__

__*Por favor enviar o fonte do programa abaixo:*__

__*Ambiente: CAMIL \- 12\.1\.2307 \(aqui informar se é CAMIL, CICLO ou HCM\)*__

__*Fonte: esp/esft1008\.p \(informar o caminho completo do fonte\)*__

__*Obrigado,*__

\*Em caso de urgência acionar o Gabriel via chat\.

  
  


2 \- Teste das alterações realizadas pelo analista/desenvolvedor\(somente específicos\)

Para testes das alterações realizadas será necessário utilizar o propath local do analista, portanto é proibido colocar os programas para testes no propath oficial do ambiente de homologação da Camil, exceto para testes de integrações com outros sistemas e rpw, para estes casos deverá ser solicitado via email, para Vera Lucia Woitexen \([vera\.woitexen@totvs\.com\.br](mailto:vera.woitexen@totvs.com.br)\) a liberação dos programas na pasta oficial do ambiente de homologação da Camil, na ausência da Vera a solicitação deverá ser realizada para Gabriel Shiratori \([gabriel\.shiratori@totvs\.com\.br](mailto:gabriel.shiratori@totvs.com.br)\)\. Obs\.: O pacote já deverá estar compilado e com a estrutura de pastas correta apenas para ser colocado na pasta\.

 

Exemplo solicitação de exceção

__*Assunto: Baixa de pacote AMB6 Camil*__

__*Bom dia Vera,*__

__*Por favor, liberar o pacote anexo no ambiente de homologação da Camil para testes de RPW\.*__

__*Anexar o pacote\.*__

__*Obrigado,*__

__*	*__

\* Os acessos ao diretório do ambiente oficial de homologação serão revisados e liberados somente para alguns analistas\.

  


3 \- Atualização do fonte TFS/Azure Totvs

Após fim dos testes internos, os fontes deverão ser atualizados no TFS/Azure da Totvs, antes da solicitação de deploy no Azure da Camil\.

  


4 \- Liberação para testes dos usuários\(somente específicos\)

Após conclusão dos testes internos, deverá ser solicitado o deploy dos programas via e\-mail para Luciano Mengarda \(luciano\.mengarda@dwcconsult\.com\.br\) conforme exemplo abaixo, para que o programa seja disponibilizado para os testes do usuário\. Na ausência do Luciano Mengarda, a solicitação deverá ser feita para Gabriel Shiratori\([gabriel\.shiratori@totvs\.com\.br](mailto:gabriel.shiratori@totvs.com.br)\)\. 

Exemplo solicitação de deploy

__*ASSUNTO: Solicitação de DEPLOY \- AMBIENTE 6 CAMIL \- GSD\-123456 \(informar o ambiente\(Ex\.: Ambiente 6 CAMIL ou Ambiente 6 CICLO\) e o ticket da Camil no assunto\)*__

__*Boa tarde Luciano,*__

__*Favor efetuar o deploy dos programas anexo no ambiente 6 da Camil\.*__

__*Obrigado,*__

Neste momento será necessário alterar o status do ticket no Jira da Camil para Paralisado informando o texto padrão abaixo\. 

Exemplo Texto Padrão

	__*Ticket paralisado aguardando aprovação da Camil para liberação dos testes\.*__

__*Usuário\(informar o nome do usuário\): Seu ticket está em fase final de liberação, por favor aguarde, pois em breve você será notificado para efetuar os testes da sua solicitação\.*__

__*Att,*__

__*Joao da Silva*__

__*AMS Totvs*__

Após a aprovação do deploy pelo analista da Camil, você será notificado por email e deverá alterar o status do Jira da Camil para AGUARDANDO TESTES informando ao usuário que o programa está disponível para testes no ambiente X\(informar o ambiente\) e liberar o pacote com os programas e o documento de liberação conforme abaixo\.

\([https://docs\.google\.com/document/d/1nJ\_fKdW4j4hCVffQSnxju2dCfY7lxPrr/edit?usp=sharing&ouid=113773414673851785174&rtpof=true&sd=true](https://docs.google.com/document/d/1nJ_fKdW4j4hCVffQSnxju2dCfY7lxPrr/edit?usp=sharing&ouid=113773414673851785174&rtpof=true&sd=true)\)\.

5 \- Status do ticket no Jira

__Status “AGUARDANDO CLIENTE”: __Os tickets com este status são encerrados automaticamente em 16 horas úteis\. Desta forma deverá ser incluída antes da assinatura a mensagem abaixo:

 

Estamos no aguardo de sua resposta para dar continuidade ao atendimento deste chamado\. Caso ela não ocorra no intervalo de 16 \(Dezesseis\) horas úteis a contar a partir desta mensagem, entenderemos que seu questionamento foi respondido e o mesmo será encerrado\.

__Status “AGUARDANDO TESTE”: __É usado quando tem liberação de pacote\. Pode ser usado também quando solicitamos algo ao usuário e sabemos que é algo demorado e ele não conseguirá fazer em 16h, caso contrário, deve ficar como __AGUARDANDO CLIENTE\.__

__Retrofit e Pequenas melhorias__

Esta atividade somente poderá ser realizada se tiver aprovação do CP do cliente Alexandre ou do Francisco\.

__Atendimento Retrofit __

Quando solicitado retrofit, deve ser alinhado com CP do cliente \(Alexandre/Francisco\)\. Neste caso, vamos precisar de uma estimativa de horas, onde iremos avaliar a aprovação para seguirmos com a atividade\. A estimativa deverá ser enviada por e\-mail para o CP do cliente copiando o Francisco\.

__Atendimento Melhorias __

Quando identificado no atendimento que se trata de uma melhoria deverá retornado no ticket o texto abaixo:

"Prezado cliente, após análise identificamos que não se trata de um erro/suporte e sim de uma melhoria no sistema\. Esta melhoria terá um custo adicional e caso deseje receber um orçamento nos retorne este ticket para providenciarmos a elaboração do mesmo\.

Atenciosamente,

TOTVS AMS"

Caso o ticket retorne informando que gostaria de receber o orçamento, deverá ser realizada uma estimativa para o desenvolvimento dessa melhoria e uma breve descrição do escopo \(incluindo um resumo da alteração que será efetuada\) e enviado por e\-mail para CP do cliente \(Alexandre\) copiando o Francisco para avaliarmos a aprovação e seguirmos com a atividade\. 

Permanecendo dúvidas consultar:

Vera Lucia Woitexen

Alexandre de Oliveira

Francisco Chaicka Junior


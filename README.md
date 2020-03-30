# Legends-of-Code-Magic
[Legends-of-Code-Magic](https://www.codingame.com/multiplayer/bot-programming/legends-of-code-magic) (LOCM) is a card game takes place between two players, and is a turn-based, zero-sum game without the possibility to tie. Each player build its own deck of cards chosen from the available choices.<br>
## Bot programming
There are several files of the agent we created:<br>
* Card_list
  * This text file contains all cards information of newest version, which is referenced from [external resources of LOCM](https://jakubkowalski.tech/Projects/LOCM/).
* Card_items
  * This text file contains item cards information.
* Card_creatures
  * This text file contains creature cards information.
* Card_value_items
  * This file analyzes the value of all items based on several empirical formula of HearthStone and Gwent Card which are both famous Trading Card Game (TCG).
  * Reference: <br>[炉石传说卡牌价值体系说明](https://zhuanlan.zhihu.com/p/37299343)<br>[《炉石传说-女巫森林》的奇偶数卡组，到底哪个厉害？](https://zhuanlan.zhihu.com/p/35233008)<br>[炉石传说从基础牌组仆从看炉石仆从牌价值体系](https://m.paopaoche.net/new/30413)<br>[通过《昆特牌》的规则与机制，研究TCG游戏设计](https://www.gameres.com/788575.html)
* Card_value_creatures
* Simple_Agent_based_on_cardvalue
* Aggro_Agent_based_on_cardvalue
* Aggro_Agent_based_on_cardvalue_modified

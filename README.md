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
  * This file analyzes the value of all items based on several empirical formula of HearthStone and Quintet which are both famous Trading Card Game (TCG).
  * Reference: <br>[Introduction of card value system of HearthStone](https://zhuanlan.zhihu.com/p/37299343)<br>[Analyze minion value system of HearthStone via basic minion of basic decks](https://m.paopaoche.net/new/30413)<br>[Analyze odd-even numbers deck by genetic algorithm](https://zhuanlan.zhihu.com/p/35233008)<br>[Studying TCG game design through the rules and mechanics of Quintet](https://www.gameres.com/788575.html)
* Card_value_creatures
* Simple_Agent_based_on_cardvalue
* Aggro_Agent_based_on_cardvalue
* Aggro_Agent_based_on_cardvalue_modified

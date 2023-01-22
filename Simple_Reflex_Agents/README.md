[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/LeandroTeixeira/learning-AI/tree/main/Simple_Reflex_Agents/README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)]https://github.com/LeandroTeixeira/learning-AI/tree/main/Simple_Reflex_Agents/README.pt-br.md)

# Simple Reflex Agent

#### _Under Development_

## Description

A Simple Reflex Agent behaves like a robot that can do simple tasks. You can give it some simple rules, like if it sees
a red ball it should pick it up, or if it sees a green
ball it should leave it alone. The robot follows these rules to make decisions and do the task.

Simple reflex agents are just like that toy robot, they follow a set of simple rules to make decisions and take
actions. They are called simple because they only consider their current perception and don't take into account their
experiences or the future outcomes.

## Algorithm

The algorithm is the implementation of Russell and Norvig's pseudocode as described in _Artificial Intelligence: A
Modern Approach_.
The agent persists the rules and a function to interpret inputs. It also has a name variable that has no impact in the
algorithm besides making it easier to identify the agent in a multi-agent context.

Their action function receives the perception as a parameter. The agent will use the interpreter function to understand
the state.
The state will then be used to identify the rule to be returned.

In this implementation, the perception can be in any format as long as the interpreter can understand it. The act
function will return another function but it will _not_ execute it right away.

## References and suggested sources

Russell, Norvig _Artificial Intelligence: A Modern Approach, 4th edition, Pearson_

[types of AI agents | Part-1/2 | simple & model based reflex | Lec-6| Bhanu Priya](https://www.youtube.com/watch?v=rWh9cK0ycuw)

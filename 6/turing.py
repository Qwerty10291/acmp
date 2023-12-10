class TuringMachine:
    def __init__(self, tape, initial_state, transitions, accepting_states):
        self.tape = list(tape)
        self.head = 0
        self.state = initial_state
        self.transitions = transitions
        self.accepting_states = accepting_states

        self.states_counter = {tr[0]: 0 for tr in transitions}
        self.rotations_counter = 0
        self.j_counter = 0
        self.symbols_counter = []

    def step(self):
        current_symbol = self.tape[self.head]
        if (self.state, current_symbol) in self.transitions:
            if self.state == "q2" and current_symbol == "0":
                self.j_counter  += 1

            transition = self.transitions[(self.state, current_symbol)]
            if self.head < 0:
                self.tape.insert(0, transition[0])
            elif self.head >= len(self.tape):
                self.tape.append(transition[0])
            else:
                self.tape[self.head] = transition[0]
                
            if transition[2] == 'П':
                self.head += 1
                self.rotations_counter += 1
            elif transition[2] == 'Л':
                self.head -= 1
                self.rotations_counter += 1
                
            self.state = transition[1]
            self.states_counter[transition[1]] += 1
            return True
        else:
            return False

    def run(self, max_steps:int):
        i = 0
        while self.state not in self.accepting_states and i < max_steps:
            if not self.step():
                break
            i += 1
            if i % 10 == 0:
                self.symbols_counter.append(self.tape[0])
        print(i)
            
    def get_tape_content(self):
        return ''.join(self.tape)

def read_transitions():
    states = input("введите список состояний(через пробел):").split()
    alphabet = input("введите символы алфавита(через пробел):").split()
    transitions = {}
    for s in states:
        for a in alphabet:
            transitions[(s, a)] = input(f"введите правило перехода для {s}-{a} (пример '0 q2 Л'):").split()

    return transitions

# Пример использования эмулятора машины Тьюринга
initial_state = input("введите начальное состояние машины:")
transitions = read_transitions()
tape_content = input("введите начальное состояние поля:")

accepting_states = {"!"}

tm = TuringMachine(tape_content, initial_state, transitions, accepting_states)
tm.run(int(input("введите максимальное количество тактов T:")))
print("a)", tm.states_counter["q1"])
print("б)", tm.states_counter)
print("в)", len(tm.tape))
print("г)", sum(1 if s != "Λ" else 0 for s in tm.tape))
print("д)", "да" if all(v > 0 for v in tm.states_counter.values()) else "нет")
print("е)", *tm.symbols_counter)
print("ж)", tm.j_counter)
print("з)", tm.rotations_counter)
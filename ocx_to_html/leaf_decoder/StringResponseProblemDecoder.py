import xml.etree.ElementTree as ET


class StringResponseProblemDecoder:
    @staticmethod
    def tohtml(paths, name):
        path = paths.check_url('problem', name )

        answers = []
        wrong_answers = []
        hints_list = []
        question_start = ""
        question_end = " ___________"

        front_stuff = ""
        correct_blob = ""

        tree = ET.parse(path)
        root = tree.getroot()

        stringresponse_elements = root.findall("./stringresponse")
        if len(stringresponse_elements) == 1:
            stringresponse_elements = stringresponse_elements[0]

        if 'answer' in stringresponse_elements.attrib:
            answers.append(stringresponse_elements.attrib['answer'])
        for child in stringresponse_elements:
            if child.tag.lower() == 'additional_answer':
                if 'answer' in child.attrib:
                    answers.append(child.attrib['answer'])
            elif child.tag.lower() == 'label':
                front_stuff += child.text
            elif child.tag.lower() == 'description':
                question_start = child.text
            elif child.tag.lower() == 'textline':
                if 'trailing_text' in child.attrib:
                    question_end += ' ' + child.attrib['trailing_text']
            elif child.tag.lower() == 'correcthint':
                correct_blob = ""
                if 'label' in child.attrib:
                    correct_blob += 'Correct' + ' - ' + child.attrib['label'] + ' '
                correct_blob += child.text
            elif child.tag.lower() == 'stringequalhint':
                wrong = {'blob': '', 'answer': ''}
                if 'label' in child.attrib:
                    wrong['blob'] += 'Incorrect' + ' - ' + child.attrib['label'] + ' '
                else:
                    wrong['blob'] += 'Incorrect' + ' '
                if 'answer' in child.attrib:
                    wrong['blob'] += child.text
                    wrong['answer'] = child.attrib['answer']
                    wrong_answers.append(wrong)

        for child in root:
            if child.tag.lower() == 'demandhint':
                hints = child.findall("./hint")
                for hint in hints:
                    hints_list.append(hint.text)

        blob = '<h2>Fill in the blank problem:</h2>'
        blob += '<div>' + front_stuff + '</div>'
        blob += '<div>'
        blob += question_start + question_end
        blob += '</div>'

        if hints_list:
            blob += '<h3>Hints:</h3>'
            for hint in hints_list:
                blob += '<div>' + hint + '</div>'

        blob += '<h3>Answers:</h3>'
        if wrong_answers:
            for wrong in wrong_answers:
                blob += '<div><b>' + wrong['answer'] + ':</b> ' + wrong['blob'] + '</div>'
        blob += '<div><b>' + ', '.join(answers) + ':</b> ' + correct_blob + '</div>'

        blob += '</p>'

        print("*** adding data from: " + path)
        print("******************************************************")
        return blob


'''
<problem display_name="Is this ever seen?">
  <stringresponse answer="GX" type="ci regexp">
    <additional_answer answer="Pokémon GX"/>
    <additional_answer answer="Pokemon GX"/>
    
    <label>
        What kinds of Pokémon are conidered the most powerful in Pokémon Sun &amp; Moon? These are Pokémon that have moves that can only be used once per game.
    </label>
    <description>
        Generally, the strongest Pokémon in the Sun &amp; Moon set are
    </description>
    <textline size="20" trailing_text="Pokémon" />
    
    
    <correcthint label="Great job!">
        Pokémon GX are considered the strongest. Some of the non-GX pokemon are strong as well and have interesting abilities.
    </correcthint>

    <stringequalhint answer="EX" label="Almost.">
        EX Pokémon were considered strong in sets before Sun &amp; Moon.
    </stringequalhint>
    <stringequalhint answer="Mega Evolution" label="Not what we had in mind.">
        Mega Evolution Pokémon were considered strong in sets before Sun &amp; Moon.
    </stringequalhint>
    <stringequalhint answer="Mega" label="Not what we had in mind.">
        Mega Evolution Pokémon were considered strong in sets before Sun &amp; Moon.
    </stringequalhint>
    <stringequalhint answer="M" label="Not what we had in mind.">
        Mega Evolution Pokémon were considered strong in sets before Sun &amp; Moon.
    </stringequalhint>
    <stringequalhint answer="Break" label="Not what we had in mind.">
        Pokémon Break were considered strong in sets before Sun &amp; Moon.
    </stringequalhint>
    
  </stringresponse>

  <demandhint>
    <hint>Solgaleo is this kind of Pokémon.</hint>
    <hint>Lunala is this kind of Pokémon.</hint>
  </demandhint>
</problem>
'''

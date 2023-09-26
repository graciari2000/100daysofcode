func textToBinary(text: String) -> String {
    let binaryArray = text.utf8.map { String($0, radix: 2, uppercase: false) }
    return binaryArray.joined(separator: " ")
}

func binaryToText(binary: String) -> String {
    let binaryComponents = binary.split(separator: " ")
    var text = ""
    for binaryChar in binaryComponents {
        if let decimalValue = Int(binaryChar, radix: 2) {
            if let unicodeScalar = UnicodeScalar(decimalValue) {
                text.append(Character(unicodeScalar))
            }
        }
    }
    return text
}

let inputText = "Hello, World!"
let binaryRepresentation = textToBinary(text: inputText)
let convertedText = binaryToText(binary: binaryRepresentation)

print("Input Text: \(inputText)")
print("Binary Representation: \(binaryRepresentation)")
print("Converted Text: \(convertedText)")
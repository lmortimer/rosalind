let inputSequence = "GACCTCGCTAGTAGAGCCCCGAGAAGCGCCTACTTGCGGTAAGAACGAAAATATGCGTCGCAGTGTTCAGAAAGCTATTGCTCGCGCACCTTATGAGCACGGCTTGATGCGCCAGAATTGGGGGAATGGGAGCTTAGGTATCATCGCGACCGCAAAGGTCATCTCCGGCCCCTACACTTGTTTTATCGTCTACCTTAATCAGTCCATATCATTAAGGCAAGCTCCAATGAGTATTAACTGGTTAGTTTGATAGCATCCGGTCCTAGCTCGAAGGGAGGTGGTGTCGGCCGTATCTGAAATAACTAATCTTCCGAGTTCCTCGGAGATTTCCGCGAATTCCTTCGCCATAGCGCAATCTAGTTCCTAGATTCAGAACGATCTGCAGCAAAGATCTCACACAGAATCGGCTCAGAGACAAGGGCACTACAATAAGACTGGCTATAACAGCGGCGCGATAGAGTTGGTATGAACCTTAGTTAGCCCGGTGACCAGACATAAGAGAAATTACTCCGTACATGCACACTCGCCGTTGAGTTCGGACCTAGAAAGCCTGCTTCATAGCCTGTGTCAGTTTCGCTGATGACGACCACGGTTGGAGTCGACGCATTCCCATTGAAGTAGGTGCTACACTAAGCTGCCGGGGAACCGCGTGGGTCCATAGTGCGCGGTCGCTGTTACAACAGAGAGTGGTAAGTCGATGATGAGCCACATCGGGTACCACGCTACATACGTGTTTCAATCAGAAGACGGTAAGGAAGGGAATGTGGTGGGCTATGGACTGATGTCGGCTCTCACCCCGTATTACT"

type NucleotideCount = {
    a: int
    c: int
    g: int
    t: int
}

let countNucleotides (input:string) = 
    // Count the number of times A, C, G, T are in the input string 
    
    let sequence = List.ofSeq input
    
    let a = sequence |> List.filter (fun c -> c = 'A') |> List.length
    let t = sequence |> List.filter (fun c -> c = 'T') |> List.length
    let g = sequence |> List.filter (fun c -> c = 'G') |> List.length
    let c = sequence |> List.filter (fun c -> c = 'C') |> List.length
    
    { a=a; c=c; g=g; t=t }
    
let nucleotideCount = countNucleotides inputSequence
    
printfn "%d %d %d %d" nucleotideCount.a nucleotideCount.c nucleotideCount.g nucleotideCount.t
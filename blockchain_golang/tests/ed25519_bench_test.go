package tests

// const (
// 	numSignatures   = 10000
// 	signaturesPerGo = 1000
// 	numGoroutines   = numSignatures / signaturesPerGo
// )

// var (
// 	publicKeys []string
// 	messages   []string
// 	signatures []string
// )

// func init() {

// 	fmt.Printf("GOMAXPROCS = %d\n", runtime.GOMAXPROCS(0))

// 	publicKeys = make([]string, numSignatures)
// 	messages = make([]string, numSignatures)
// 	signatures = make([]string, numSignatures)

// 	mnemonic := "smoke suggest security index situate almost ethics tone wash crystal debris mosquito pony extra husband elder over relax width occur inspire keen sudden average"
// 	mnemonicPassword := ""
// 	bip44Path := []uint32{44, 7331, 0, 0}

// 	var wg sync.WaitGroup
// 	wg.Add(numGoroutines)

// 	for g := 0; g < numGoroutines; g++ {
// 		go func(goroutineIndex int) {
// 			defer wg.Done()

// 			start := goroutineIndex * signaturesPerGo
// 			end := start + signaturesPerGo

// 			for i := start; i < end; i++ {
// 				keypair := ed25519.GenerateKeyPair(mnemonic, mnemonicPassword, bip44Path)

// 				message := "Message number #" + string(rune(i))
// 				signature := ed25519.GenerateSignature(keypair.Prv, message)

// 				publicKeys[i] = keypair.Pub
// 				messages[i] = message
// 				signatures[i] = signature
// 			}
// 		}(g)
// 	}

// 	wg.Wait()
// 	fmt.Println("===============Finished===============")
// }

// func BenchmarkEd25519VerifyParallel100x1000(b *testing.B) {
// 	b.ResetTimer()

// 	b.RunParallel(func(pb *testing.PB) {
// 		for pb.Next() {
// 			var wg sync.WaitGroup
// 			wg.Add(numGoroutines)

// 			for g := 0; g < numGoroutines; g++ {
// 				go func(goroutineIndex int) {
// 					defer wg.Done()
// 					start := goroutineIndex * signaturesPerGo
// 					end := start + signaturesPerGo

// 					for j := start; j < end; j++ {
// 						if !ed25519.VerifySignature(messages[j], publicKeys[j], signatures[j]) {
// 							b.Fatalf("Signature verification failed at index %d", j)
// 						}
// 					}
// 				}(g)
// 			}

// 			wg.Wait()
// 		}
// 	})
// }

package structures

type Transaction struct {
	V       uint           `json:"v"`
	Fee     string         `json:"fee"`
	Creator string         `json:"creator"`
	Sig     string         `json:"sig"`
	Type    string         `json:"type"`
	SigType string         `json:"sigType"`
	Nonce   int            `json:"nonce"`
	Payload map[string]any `json:"payload"`
}

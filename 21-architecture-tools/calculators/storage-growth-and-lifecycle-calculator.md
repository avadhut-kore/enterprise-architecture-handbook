# Storage Growth & Lifecycle Tiering Calculator

## Formula
$$\text{Monthly Cost} = (\text{GB}_{\text{Standard}} \times \$0.023) + (\text{GB}_{\text{Infrequent}} \times \$0.0125) + (\text{GB}_{\text{Glacier}} \times \$0.0036)$$
- Implementing automated lifecycle rules transitioning 80% of data to Glacier after 90 days reduces annual storage spend by over 75%.
